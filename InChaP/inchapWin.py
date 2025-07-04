from PySide6 import QtWidgets
from guidata.ui_main import Ui_MainWindow
from guidata import *

import os
import zipfile
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import re
from math import log10

class MainWindow(QtWidgets.QMainWindow):

     #////////////////////////////////// UI FUNCTIONS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.close_shortcut = QShortcut(QKeySequence('Ctrl+W'), self)
        self.close_shortcut.activated.connect(self.close_app)

    
        #//////////////////////////////////////// VARIABLES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

        self.N_AVAGADRO = 6.02214076e23
        self.data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
        # self.results_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Results')
        self.results_folder = os.path.join('C:\\', 'Results') # Change this line for Windows app



        #//////////////////////////////////////// TABLE WIDGETS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

        self.ui.tableWidget_Results.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        

        #//////////////////////////////////////// UI BUTONS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

        



        #//////////////////////////////////////// APP BUTONS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

        self.ui.BtnCalculate.clicked.connect(self.calculate)
        self.ui.CmbChemical.currentIndexChanged.connect(self.pages_formula)
        self.ui.CmbMethod.currentIndexChanged.connect(self.pages_formula)
        self.ui.CmbEnergy.currentIndexChanged.connect(self.pages_energy)
        self.ui.BtnDownload.clicked.connect(self.export_results)
        

        #//////////////////////////////////////// START FUNCTIONS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
        
        if not os.path.exists(self.results_folder):
            os.makedirs(self.results_folder)
        
        try:
            self.atomic_numbers, self.mass_numbers = self.read_phyconst(self.data_folder)
        except Exception as e:
            self.ui.label_2.setText("Error reading phyconst.csv")
            return

    #//////////////////////////////////////// APP FUNCTIONS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def close_app(self):
        """Close the application."""
        self.close()

    def calculate(self):
        sent_ion = self.ui.CmbSentIon.currentText() 
        self.ui.tableWidget_Variables.setItem(0, 1, QtWidgets.QTableWidgetItem(sent_ion)) 

        if self.ui.CmbEnergy.currentIndex() == 1:
            row_count = self.ui.tableWidget_Variables.rowCount()  
            for row in range(row_count):
                self.ui.tableWidget_Variables.setItem(row, 0, QtWidgets.QTableWidgetItem("All"))  
        else:
            row_count = self.ui.tableWidget_Variables.rowCount()  
            energy_value = self.ui.LneEnergy.text()  
            for row in range(row_count):
                self.ui.tableWidget_Variables.setItem(row, 0, QtWidgets.QTableWidgetItem(energy_value)) 
    
        # RSP FORMULA
        if self.ui.CmbMethod.currentIndex() == 0 and self.ui.CmbChemical.currentIndex() == 0:
            material_1_formula = self.ui.LneChemicalFormula1.text() 
            material_2_formula = self.ui.LneChemicalFormula2.text() 

            

            if self.ui.CmbEnergy.currentIndex() == 0:
                energy = float(self.ui.LneEnergy.text())
                self.CMSPRTDMFSE_compound(sent_ion, material_1_formula, material_2_formula, energy, self.atomic_numbers, self.mass_numbers, self.data_folder, self.results_folder)
            else:
                self.CMSPRTDMFAE_compound(sent_ion, material_1_formula, material_2_formula, self.atomic_numbers, self.mass_numbers, self.data_folder, self.results_folder)

        # MSP FORMULA
        if self.ui.CmbMethod.currentIndex() == 1 and self.ui.CmbChemical.currentIndex() == 0:
            target_formula = self.ui.LneChemicalFormula.text() 

            if self.ui.CmbEnergy.currentIndex() == 0:
                energy = float(self.ui.LneEnergy.text())
                self.process_single_energy_compound(sent_ion, target_formula, energy, self.atomic_numbers, self.mass_numbers, self.data_folder, self.results_folder)
            else:
                self.process_all_energies_compound(sent_ion, target_formula, self.atomic_numbers, self.mass_numbers, self.data_folder, self.results_folder)


        # RSP COMPOSITION
        if self.ui.CmbMethod.currentIndex() == 0 and self.ui.CmbChemical.currentIndex() == 1:
            material_1_formula = self.ui.LneElements1.text() 
            material_2_formula = self.ui.LneElements2.text()
        
            if self.ui.CmbEnergy.currentIndex() == 0:
                energy = float(self.ui.LneEnergy.text())
                self.CMSPRTDMFSE_composition(sent_ion, material_1_formula, material_2_formula, energy, self.atomic_numbers, self.mass_numbers, self.data_folder, self.results_folder)
            else:
                self.CMSPRTDMFAE_composition(sent_ion, material_1_formula, material_2_formula, self.atomic_numbers, self.mass_numbers, self.data_folder, self.results_folder)



        # MSP COMPOSITION
        if self.ui.CmbMethod.currentIndex() == 1 and self.ui.CmbChemical.currentIndex() == 1:
            target_formula = self.ui.Lneacomposition.text()
            
            if self.ui.CmbEnergy.currentIndex() == 0:
                energy = float(self.ui.LneEnergy.text())
                self.process_single_energy_composition(sent_ion, target_formula, energy, self.atomic_numbers, self.mass_numbers, self.data_folder, self.results_folder)
            else:
                self.process_all_energies_composition(sent_ion, target_formula, self.atomic_numbers, self.mass_numbers, self.data_folder, self.results_folder)

    def export_results(self):
        row_count_formula = self.ui.tableWidget_Chemical_Formula.rowCount()
        results_folder = self.results_folder
        sent_ion = self.ui.CmbSentIon.currentText()

        if row_count_formula == 2:
            material_1_formula = self.ui.tableWidget_Chemical_Formula.item(0, 0).text()
            material_2_formula = self.ui.tableWidget_Chemical_Formula.item(1, 0).text()

            energies = []
            rsp_values = []


            for row in range(self.ui.tableWidget_Results.rowCount()):
                energy = self.ui.tableWidget_Results.item(row, 0).text()  
                rsp = self.ui.tableWidget_Results.item(row, 1).text()  
                energies.append(energy)
                rsp_values.append(rsp)


            data = {
                'Sent Ion': [sent_ion] * len(energies),
                'Material 1 Formula': [material_1_formula] * len(energies),
                'Material 2 Formula': [material_2_formula] * len(energies),
                'Energy': energies,
                'RSP': rsp_values
            }

            df = pd.DataFrame(data)

            file_name = f"RSP_{material_1_formula}_{material_2_formula}.xlsx"
            file_path = os.path.join(results_folder, file_name)


            df.to_excel(file_path, index=False)
            self.ui.label_2.setText(f"Results saved to {file_path}")


        elif row_count_formula == 1:
            target_formula = self.ui.tableWidget_Chemical_Formula.item(0, 0).text()

            energies = []
            msp_targets = []
            sigma_targets = []
            z_effs = []
            n_es = []
            wrsp_targets = []

            for row in range(self.ui.tableWidget_Results.rowCount()):
                energy = self.ui.tableWidget_Results.item(row, 0).text()  
                msp_target = self.ui.tableWidget_Results.item(row, 1).text()  
                sigma_target = self.ui.tableWidget_Results.item(row, 2).text() 
                z_eff = self.ui.tableWidget_Results.item(row, 3).text()  
                n_e = self.ui.tableWidget_Results.item(row, 4).text()  
                wrsp_target = self.ui.tableWidget_Results.item(row, 5).text()  

                energies.append(energy)
                msp_targets.append(msp_target)
                sigma_targets.append(sigma_target)
                z_effs.append(z_eff)
                n_es.append(n_e)
                wrsp_targets.append(wrsp_target)

            data = {
                'Sent Ion': [sent_ion] * len(energies),
                'Target Formula': [target_formula] * len(energies),
                'Energy': energies,
                'MSP Target': msp_targets,
                'Sigma Target': sigma_targets,
                'Z_eff': z_effs,
                'N_e': n_es,
                'WRSP Target': wrsp_targets
            }

            df = pd.DataFrame(data)

            file_name = f"{sent_ion}_to_{target_formula}.xlsx"
            file_path = os.path.join(results_folder, file_name)

            df.to_excel(file_path, index=False)
            self.ui.label_2.setText(f"Results saved to {file_path}")

        else:
            self.ui.label_2.setText("Invalid number of rows in tableWidget_Chemical_Formula.")

            

        

    def parse_formula(self, formula):
        pattern = r'([A-Z][a-z]?)(\d*)'  
        constituents = re.findall(pattern, formula)
        compound = {}
        for (element, count) in constituents:
            if count == '':
                count = 1
            else:
                count = int(count)
            if element in compound:
                compound[element] += count
            else:
                compound[element] = count
        return compound
    
    def parse_composition(self, composition):
        pattern = r'([0-9]*\.?[0-9]+)([A-Z][a-z]?)'  
        constituents = re.findall(pattern, composition)
        chemical_composition = {}
        
        for coeff, element in constituents:
            coeff = float(coeff)
            if element in chemical_composition:
                chemical_composition[element] += coeff
            else:
                chemical_composition[element] = coeff
        
        return chemical_composition

    def read_phyconst(self, data_folder):
        phyconst_path = os.path.join(data_folder, 'phyconst.csv')
        df = pd.read_csv(phyconst_path, header=None, names=['Element', 'Z', 'A'])
        atomic_numbers = df.set_index('Element')['Z'].to_dict()
        mass_numbers = df.set_index('Element')['A'].to_dict()
        return atomic_numbers, mass_numbers

    def get_msp(self, sent_ion, element, energy, data_folder):
        sention_folder = os.path.join(data_folder, f"{sent_ion}-data")
        element_csv = os.path.join(sention_folder, f"{element}.csv")
        if not os.path.exists(element_csv):
            raise FileNotFoundError(f"{element_csv} does not exist.")
        df = pd.read_csv(element_csv, header=None, names=['Energy', 'MSP', 'Projected Range', 'Longitudinal Straggling', 'Lateral Straggling'])
        if energy in df['Energy'].values:
            msp = df.loc[df['Energy'] == energy, 'MSP'].values[0]
        else:
            energies = df['Energy'].values
            msps = df['MSP'].values
            if energy < energies.min() or energy > energies.max():
                raise ValueError(f"Energy {energy} MeV is out of bounds for interpolation in {element}.csv. \n The energy value you enter must meet the range {energies.min()} < energy < {energies.max()} \n")
            log_energies = np.log(energies)
            log_msps = np.log(msps)
            log_energy = np.log(energy)
            log_interp_func = interp1d(log_energies, log_msps, kind='linear', fill_value="extrapolate")
            log_msp_interpolated = log_interp_func(log_energy)
            msp = np.exp(log_msp_interpolated)
        return msp

    def calculate_weights_compound(self, compound, mass_numbers):
        total = sum(count * mass_numbers[element] for element, count in compound.items())
        weights = {element: (count * mass_numbers[element]) / total for element, count in compound.items()}
        return weights

    def calculate_weights_composition(self, composition):
        weights = {element: coeff for element, coeff in composition.items()}
        return weights

    def calculate_msp_target_compound(self, compound, weights, msp_values):
        msp_target = sum(msp_values[element] * weights[element] for element in compound)
        return msp_target

    def calculate_msp_target_composition(self, composition, weights, msp_values):
        msp_target = sum(msp_values[element] * weights[element] for element in composition)
        return msp_target

    def calculate_sigma_target(self, msp_target, weights, mass_numbers):
        denominator = sum(weights[element] / mass_numbers[element] for element in weights)
        sigma_target = (1e24 * (msp_target)) / (self.N_AVAGADRO * denominator)
        return sigma_target

    def calculate_sigma_element(self, sent_ion, element, energy, mass_numbers, data_folder):
        msp_element = self.get_msp(sent_ion, element, energy, data_folder)
        sigma_element = (msp_element * mass_numbers[element] *1e24) / self.N_AVAGADRO
        return sigma_element

    def calculate_elements_sigma(self, sent_ion, elements, energy, mass_numbers, data_folder, results_folder):
        sigma_values = {}
        for element in elements:
            try:
                sigma = self.calculate_sigma_element(sent_ion, element, energy, mass_numbers, data_folder)
                sigma_values[element] = sigma
            except Exception as e:
                self.ui.label_2.setText(f"Error calculating sigma for {element}: {e}")
                sigma_values[element] = np.nan

        elements_sorted = sorted(sigma_values.keys())
        sigmas_sorted = [sigma_values[el] for el in elements_sorted]

        return sigma_values

    def find_sigma_bounds(self, sigma_target, sigma_values, atomic_numbers):
        sorted_elements = sorted(sigma_values.items(), key=lambda x: x[1])
        sigma_1, sigma_2 = None, None
        Z_1, Z_2 = None, None
        for i in range(len(sorted_elements) - 1):
            element_1, sigma_low = sorted_elements[i]
            element_2, sigma_high = sorted_elements[i + 1]
            if sigma_low <= sigma_target <= sigma_high:
                sigma_1, sigma_2 = sigma_low, sigma_high
                Z_1, Z_2 = atomic_numbers[element_1], atomic_numbers[element_2]
                if Z_1 < Z_2 and sigma_1 < sigma_target < sigma_2:
                    break
        if sigma_1 is None or sigma_2 is None:
            raise ValueError("sigma_target is out of the bounds of the calculated sigma values.")

        return sigma_1, sigma_2, Z_1, Z_2

    def calculate_z_eff(self, sigma, sigma_1, sigma_2, Z_1, Z_2):
        log_sigma = log10(sigma)
        log_sigma1 = log10(sigma_1)
        log_sigma2 = log10(sigma_2)
        
        numerator = (Z_1 * (log_sigma2 - log_sigma)) + (Z_2 * (log_sigma - log_sigma1))
        denominator = (log_sigma2 - log_sigma1)
        
        Z_eff = numerator / denominator
        return Z_eff

    def calculate_n_e(self, Z_eff, W_average):
        A_average = W_average
        N_e = 6.02214076 * Z_eff / A_average
        return N_e

    def calculate_a_average(self, weights, mass_numbers):
        A_average = sum(weights[element] * mass_numbers[element] for element in weights)
        return A_average

    def calculate_msp_water(self, data_folder, sent_ion, energy):
        compound = self.parse_formula('H2O')
        try:
            atomic_numbers, mass_numbers = self.read_phyconst(data_folder)
        except Exception as e:
            self.ui.label_2.setText(f"Error reading phyconst.csv: {e}")
            return
        weights = self.calculate_weights_compound(compound, mass_numbers)
        msp_values = {}
        for element in compound:
            msp_values[element] = self.get_msp(sent_ion, element, energy, data_folder)
        msp_water = self.calculate_msp_target_compound(compound, weights, msp_values)
        return msp_water

    def pages_formula(self):
        def set_page(label_text, widget):
            self.ui.label_29.setText(label_text)
            self.ui.stackedWidget.setCurrentWidget(widget)
    
        method_index = self.ui.CmbMethod.currentIndex()
        chemical_index = self.ui.CmbChemical.currentIndex()
    
        if method_index == 0:
            if chemical_index == 0:
                set_page("Chemical Formula", self.ui.page_formula_two_mat)
            elif chemical_index == 1:
                set_page("Chemical Composition", self.ui.page_two_composition)
        elif method_index == 1:
            if chemical_index == 0:
                set_page("Chemical Formula", self.ui.page_formula_a_mat)
            elif chemical_index == 1:
                set_page("Chemical Composition", self.ui.page_a_composition)

    def pages_energy(self):
        if self.ui.CmbEnergy.currentIndex() == 0:
            self.ui.stackedWidget_2.setCurrentIndex(1)
        else:
            self.ui.stackedWidget_2.setCurrentIndex(0)

    #RSP FORMULA SINGLE
    #Calculate MSP Ratios of two different materials for single energy (compound)
    def CMSPRTDMFSE_compound(self, sent_ion, material_1_formula, material_2_formula, energy, atomic_numbers, mass_numbers, data_folder, results_folder):

        compound_1 = self.parse_formula(material_1_formula)
        compound_2 = self.parse_formula(material_2_formula)

        weights_1 = self.calculate_weights_compound(compound_1, mass_numbers)
        weights_2 = self.calculate_weights_compound(compound_2, mass_numbers)

        msp_values_1 = {}
        for element_1 in compound_1:
            msp_values_1[element_1] = self.get_msp(sent_ion, element_1, energy, data_folder)

        msp_values_2 = {}
        for element_2 in compound_2:
            msp_values_2[element_2] = self.get_msp(sent_ion, element_2, energy, data_folder)

        msp_1 = self.calculate_msp_target_compound(compound_1, weights_1, msp_values_1)
        msp_2 = self.calculate_msp_target_compound(compound_2, weights_2, msp_values_2)
        ratio = msp_1 / msp_2
        self.ui.label_2.setText(f"MSP ratio of {material_1_formula} / {material_2_formula} = {ratio}")

        self.ui.tableWidget_Chemical_Formula.setRowCount(0)
        row_count = self.ui.tableWidget_Chemical_Formula.rowCount()
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(material_1_formula)))
        row_count += 1 
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(material_2_formula)))

        self.ui.tableWidget_Results.setRowCount(0)
        self.ui.tableWidget_Results.setColumnCount(2)  
        self.ui.tableWidget_Results.setHorizontalHeaderLabels(["Energy", "RSP"])  


        row_count = self.ui.tableWidget_Results.rowCount() 
        self.ui.tableWidget_Results.insertRow(row_count)  

        self.ui.tableWidget_Results.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(energy)))
        self.ui.tableWidget_Results.setItem(row_count, 1, QtWidgets.QTableWidgetItem(f"{ratio}"))

    #RSP COMPOSITION SINGLE
    #Calculate MSP Ratios of two different materials for single energy (composition)
    def CMSPRTDMFSE_composition(self, sent_ion, material_1_formula, material_2_formula, energy, atomic_numbers, mass_numbers, data_folder, results_folder):

        compound_1 = self.parse_composition(material_1_formula)
        compound_2 = self.parse_composition(material_2_formula)

        weights_1 = self.calculate_weights_composition(compound_1)
        weights_2 = self.calculate_weights_composition(compound_2)

        msp_values_1 = {}

        for element_1 in compound_1:
            msp_values_1[element_1] = self.get_msp(sent_ion, element_1, energy, data_folder)

        msp_values_2 = {}

        for element_2 in compound_2:
            msp_values_2[element_2] = self.get_msp(sent_ion, element_2, energy, data_folder)

        msp_1 = self.calculate_msp_target_compound(compound_1, weights_1, msp_values_1)
        msp_2 = self.calculate_msp_target_compound(compound_2, weights_2, msp_values_2)
        ratio = msp_1 / msp_2
        self.ui.label_2.setText(f"MSP ratio of {material_1_formula} / {material_2_formula} = {ratio}")

        self.ui.tableWidget_Chemical_Formula.setRowCount(0)
        row_count = self.ui.tableWidget_Chemical_Formula.rowCount()
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(material_1_formula)))
        row_count += 1 
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(material_2_formula)))

        self.ui.tableWidget_Results.setRowCount(0)
        self.ui.tableWidget_Results.setColumnCount(2)
        self.ui.tableWidget_Results.setHorizontalHeaderLabels(["Energy", "RSP"])

        row_count = self.ui.tableWidget_Results.rowCount()
        self.ui.tableWidget_Results.insertRow(row_count)

        self.ui.tableWidget_Results.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(energy)))
        self.ui.tableWidget_Results.setItem(row_count, 1, QtWidgets.QTableWidgetItem(f"{ratio}"))

        

    # RSP FORMULA ALL
    # Calculate MSP Ratios of two different materials for all energies (compound)
    def CMSPRTDMFAE_compound(self, sent_ion, material_1_formula, material_2_formula, atomic_numbers, mass_numbers, data_folder, results_folder):
        compound_1 = self.parse_formula(material_1_formula)
        compound_2 = self.parse_formula(material_2_formula)

        first_element = next(iter(compound_1))
        sention_folder = os.path.join(data_folder, f"{sent_ion}-data")
        first_element_csv = os.path.join(sention_folder, f"{first_element}.csv")

        if not os.path.exists(first_element_csv):
            raise FileNotFoundError(f"{first_element_csv} does not exist.")

        df_first = pd.read_csv(first_element_csv, header=None, names=['Energy', 'MSP', 'Projected Range', 'Longitudinal Straggling', 'Lateral Straggling'])
        energies = df_first['Energy'].unique()

        results = []

        for energy in sorted(energies):
            try:
                weights_1 = self.calculate_weights_compound(compound_1, mass_numbers)
                weights_2 = self.calculate_weights_compound(compound_2, mass_numbers)

                msp_values_1 = {}
                for element_1 in compound_1:
                    msp_values_1[element_1] = self.get_msp(sent_ion, element_1, energy, data_folder)

                msp_values_2 = {}
                for element_2 in compound_2:
                    msp_values_2[element_2] = self.get_msp(sent_ion, element_2, energy, data_folder)

                msp_1 = self.calculate_msp_target_compound(compound_1, weights_1, msp_values_1)
                msp_2 = self.calculate_msp_target_compound(compound_2, weights_2, msp_values_2)
                ratio = msp_1 / msp_2

                results.append({'sent_ion': sent_ion, 'material_1_formula': material_1_formula, 'material_2_formula': material_2_formula, 'energy': energy, 'RSP': ratio})

            except Exception as e:
                self.ui.label_2.setText(f"Error processing energy {energy} MeV: {e}")
                results.append({'sent_ion': sent_ion, 'material_1_formula': material_1_formula, 'material_2_formula': material_2_formula, 'energy': energy, 'RSP': None})

        self.ui.tableWidget_Chemical_Formula.setRowCount(0)
        row_count = self.ui.tableWidget_Chemical_Formula.rowCount()
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(material_1_formula)))
        row_count += 1
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(material_2_formula)))

        self.ui.tableWidget_Results.setRowCount(0)
        self.ui.tableWidget_Results.setColumnCount(2)  
        self.ui.tableWidget_Results.setHorizontalHeaderLabels(["Energy", "RSP"])  

        for result in results:
            energy = result['energy']
            ratio = result['RSP']
            row_count = self.ui.tableWidget_Results.rowCount()  
            self.ui.tableWidget_Results.insertRow(row_count)  

            self.ui.tableWidget_Results.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(energy)))
            if ratio is not None:
                self.ui.tableWidget_Results.setItem(row_count, 1, QtWidgets.QTableWidgetItem(f"{ratio}"))
            else:
                self.ui.tableWidget_Results.setItem(row_count, 1, QtWidgets.QTableWidgetItem("N/A"))

        self.ui.label_2.setText(f"All energy calculations completed.")

    # RSP COMPOSITION ALL
    # Calculate MSP Ratios of two different materials for all energies (composition)
    def CMSPRTDMFAE_composition(self, sent_ion, material_1_formula, material_2_formula, atomic_numbers, mass_numbers, data_folder, results_folder):
        compound_1 = self.parse_composition(material_1_formula)
        compound_2 = self.parse_composition(material_2_formula)

        first_element = next(iter(compound_1))
        sention_folder = os.path.join(data_folder, f"{sent_ion}-data")
        first_element_csv = os.path.join(sention_folder, f"{first_element}.csv")

        if not os.path.exists(first_element_csv):
            raise FileNotFoundError(f"{first_element_csv} does not exist.")

        df_first = pd.read_csv(first_element_csv, header=None, names=['Energy', 'MSP', 'Projected Range', 'Longitudinal Straggling', 'Lateral Straggling'])
        energies = df_first['Energy'].unique()

        results = []

        for energy in sorted(energies):
            try:
                weights_1 = self.calculate_weights_composition(compound_1)
                weights_2 = self.calculate_weights_composition(compound_2)

                msp_values_1 = {}
                for element_1 in compound_1:
                    msp_values_1[element_1] = self.get_msp(sent_ion, element_1, energy, data_folder)

                msp_values_2 = {}
                for element_2 in compound_2:
                    msp_values_2[element_2] = self.get_msp(sent_ion, element_2, energy, data_folder)

                msp_1 = self.calculate_msp_target_composition(compound_1, weights_1, msp_values_1)
                msp_2 = self.calculate_msp_target_composition(compound_2, weights_2, msp_values_2)
                ratio = msp_1 / msp_2

                results.append({'sent_ion': sent_ion, 'material_1_formula': material_1_formula, 'material_2_formula': material_2_formula, 'energy': energy, 'RSP': ratio})

            except Exception as e:
                self.ui.label_2.setText(f"Error processing energy {energy} MeV: {e}")
                results.append({'sent_ion': sent_ion, 'material_1_formula': material_1_formula, 'material_2_formula': material_2_formula, 'energy': energy, 'RSP': None}) 

        self.ui.tableWidget_Chemical_Formula.setRowCount(0)
        row_count = self.ui.tableWidget_Chemical_Formula.rowCount()
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(material_1_formula)))
        row_count += 1
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(material_2_formula)))

        self.ui.tableWidget_Results.setRowCount(0)
        self.ui.tableWidget_Results.setColumnCount(2)  
        self.ui.tableWidget_Results.setHorizontalHeaderLabels(["Energy", "RSP"])  

        for result in results:
            energy = result['energy']
            ratio = result['RSP']
            row_count = self.ui.tableWidget_Results.rowCount()  
            self.ui.tableWidget_Results.insertRow(row_count)  

            self.ui.tableWidget_Results.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(energy)))
            if ratio is not None:
                self.ui.tableWidget_Results.setItem(row_count, 1, QtWidgets.QTableWidgetItem(f"{ratio}"))
            else:
                self.ui.tableWidget_Results.setItem(row_count, 1, QtWidgets.QTableWidgetItem("N/A")) 

        self.ui.label_2.setText(f"All energy calculations completed.")


    # MSP FORMULA SINGLE
    def process_single_energy_compound(self, sent_ion, target_formula, energy, atomic_numbers, mass_numbers, data_folder, results_folder):
        self.ui.label_2.setText(f"\n Processing {energy} MeV energy")

        compound = self.parse_formula(target_formula)
        
        weights = self.calculate_weights_compound(compound, mass_numbers)
        
        msp_values = {}
        for element in compound:
            msp_values[element] = self.get_msp(sent_ion, element, energy, data_folder)
        
        msp_target = self.calculate_msp_target_compound(compound, weights, msp_values)
        
        msp_water = self.calculate_msp_water(data_folder, sent_ion, energy)
        
        PRSP_target = msp_target / msp_water
        
        sigma_target = self.calculate_sigma_target(msp_target, weights, mass_numbers)
        
        all_elements = [
            "Ag", "Au", "Br", "Ce", "Cs", "Eu", "Gd", "Hf", "In", "La", "Mn", "Nb", "O", "Pd", "Rb",
            "S", "Si", "Ta", "Ti", "W", "Zn", "Al", "B", "C", "Cl", "Cu", "F", "Ge", "Hg", "Ir",
            "Li", "Mo", "Nd", "Os", "Pm", "Re", "Sb", "Sm", "Tb", "Tl", "Xe", "Zr", "Ar", "Ba",
            "Ca", "Co", "Dy", "Fe", "H", "Ho", "K", "Lu", "N", "Ne", "P", "Pr", "Rh", "Sc", "Sn",
            "Tc", "Tm", "Y", "As", "Be", "Cd", "Cr", "Er", "Ga", "He", "I", "Kr", "Mg", "Na", "Ni",
            "Pb", "Pt", "Ru", "Se", "Sr", "Te", "V", "Yb"
        ]
        
        sigma_values = self.calculate_elements_sigma(sent_ion, all_elements, energy, mass_numbers, data_folder, results_folder)
        
        sigma_1, sigma_2, Z_1, Z_2 = self.find_sigma_bounds(sigma_target, sigma_values, atomic_numbers)
        
        Z_eff = self.calculate_z_eff(sigma_target, sigma_1, sigma_2, Z_1, Z_2)
        
        A_average = self.calculate_a_average(weights, mass_numbers)

        N_e = self.calculate_n_e(Z_eff, A_average)

        self.ui.tableWidget_Chemical_Formula.setRowCount(0)
        row_count = self.ui.tableWidget_Chemical_Formula.rowCount()
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(target_formula)))


        self.ui.tableWidget_Results.setRowCount(0)
        self.ui.tableWidget_Results.setColumnCount(5) 
        self.ui.tableWidget_Results.setHorizontalHeaderLabels(["Energy", "Sigma Target", "Z_eff", "N_e", "WRSP"])

        row_count = self.ui.tableWidget_Results.rowCount()
        self.ui.tableWidget_Results.insertRow(row_count)

        self.ui.tableWidget_Results.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(energy)))
        self.ui.tableWidget_Results.setItem(row_count, 1, QtWidgets.QTableWidgetItem(f"{sigma_target}"))
        self.ui.tableWidget_Results.setItem(row_count, 2, QtWidgets.QTableWidgetItem(f"{Z_eff}"))
        self.ui.tableWidget_Results.setItem(row_count, 3, QtWidgets.QTableWidgetItem(f"{N_e}"))
        self.ui.tableWidget_Results.setItem(row_count, 4, QtWidgets.QTableWidgetItem(f"{PRSP_target}"))

        # print("\n...Results...\n")
        # print(f"sent_ion : {sent_ion}")
        # print(f"target_formula : {target_formula}")
        # print(f"energy : {energy}")
        # print(f"msp_target : {msp_target}")
        # print(f"sigma_target : {sigma_target}")
        # print(f"Z_eff: {Z_eff}")
        # print(f"N_e: {N_e}")
        # print(f"(WRSP) MSP_{target_formula}/MSP_H2O : {PRSP_target}")


    # MSP COMPOSITION SINGLE
    def process_single_energy_composition(self, sent_ion, target_formula, energy, atomic_numbers, mass_numbers, data_folder, results_folder):
        self.ui.label_2.setText(f"\n Processing {energy} MeV energy")

        composition = self.parse_composition(target_formula)
        
        weights = self.calculate_weights_composition(composition)
        
        msp_values = {}
        for element in composition:
            msp_values[element] = self.get_msp(sent_ion, element, energy, data_folder)
        
        msp_target = self.calculate_msp_target_composition(composition, weights, msp_values)
        
        msp_water = self.calculate_msp_water(data_folder, sent_ion, energy)
        
        PRSP_target = msp_target / msp_water

        sigma_target = self.calculate_sigma_target(msp_target, weights, mass_numbers)
        
        all_elements = [
            "Ag","Au","Br","Ce","Cs","Eu","Gd","Hf","In","La","Mn","Nb","O","Pd","Rb",
            "S","Si","Ta","Ti","W","Zn","Al","B","C","Cl","Cu","F","Ge","Hg","Ir",
            "Li","Mo","Nd","Os","Pm","Re","Sb","Sm","Tb","Tl","Xe","Zr","Ar","Ba",
            "Ca","Co","Dy","Fe","H","Ho","K","Lu","N","Ne","P","Pr","Rh","Sc","Sn",
            "Tc","Tm","Y","As","Be","Cd","Cr","Er","Ga","He","I","Kr","Mg","Na","Ni",
            "Pb","Pt","Ru","Se","Sr","Te","V","Yb"
        ]
        
        sigma_values = self.calculate_elements_sigma(sent_ion, all_elements, energy, mass_numbers, data_folder, results_folder)
        
        sigma_1, sigma_2, Z_1, Z_2 = self.find_sigma_bounds(sigma_target, sigma_values, atomic_numbers)
        
        Z_eff = self.calculate_z_eff(sigma_target, sigma_1, sigma_2, Z_1, Z_2)
        
        A_average = self.calculate_a_average(weights, mass_numbers)

        N_e = self.calculate_n_e(Z_eff, A_average)

        self.ui.tableWidget_Chemical_Formula.setRowCount(0)
        row_count = self.ui.tableWidget_Chemical_Formula.rowCount()
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(target_formula)))

        self.ui.tableWidget_Results.setRowCount(0)
        self.ui.tableWidget_Results.setColumnCount(6)
        self.ui.tableWidget_Results.setHorizontalHeaderLabels(["Energy", "MSP Target", "Sigma Target", "Z_eff", "N_e", "WRSP"])

        row_count = self.ui.tableWidget_Results.rowCount()
        self.ui.tableWidget_Results.insertRow(row_count)

        self.ui.tableWidget_Results.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(energy)))
        self.ui.tableWidget_Results.setItem(row_count, 1, QtWidgets.QTableWidgetItem(f"{msp_target}"))
        self.ui.tableWidget_Results.setItem(row_count, 2, QtWidgets.QTableWidgetItem(f"{sigma_target}"))
        self.ui.tableWidget_Results.setItem(row_count, 3, QtWidgets.QTableWidgetItem(f"{Z_eff}"))
        self.ui.tableWidget_Results.setItem(row_count, 4, QtWidgets.QTableWidgetItem(f"{N_e}"))
        self.ui.tableWidget_Results.setItem(row_count, 5, QtWidgets.QTableWidgetItem(f"{PRSP_target}"))

        # print("\n...Results...\n")
        # print(f"sent_ion : {sent_ion}")
        # print(f"target_formula : {target_formula}")
        # print(f"energy : {energy}")
        # print(f"msp_target : {msp_target}")
        # print(f"sigma_target : {sigma_target}")
        # print(f"Z_eff: {Z_eff}")
        # print(f"N_e: {N_e}")
        # print(f"(WRSP) MSP_{target_formula}/MSP_H2O : {PRSP_target}")


    # MSP FORMULA ALL
    def process_all_energies_compound(self, sent_ion, target_formula, atomic_numbers, mass_numbers, data_folder, results_folder):
        compound = self.parse_formula(target_formula)

        first_element = next(iter(compound))
        sention_folder = os.path.join(data_folder, f"{sent_ion}-data")
        first_element_csv = os.path.join(sention_folder, f"{first_element}.csv")

        if not os.path.exists(first_element_csv):
            raise FileNotFoundError(f"{first_element_csv} does not exist.")

        df_first = pd.read_csv(first_element_csv, header=None, names=['Energy', 'MSP', 'Projected Range', 'Longitudinal Straggling', 'Lateral Straggling'])
        energies = df_first['Energy'].unique()

        results = []

        self.ui.tableWidget_Results.setRowCount(0)
        self.ui.tableWidget_Results.setColumnCount(6)  
        self.ui.tableWidget_Results.setHorizontalHeaderLabels(["Energy", "MSP Target", "Sigma Target", "Z_eff", "N_e", "WRSP"])

        for energy in sorted(energies):
            try:
                weights = self.calculate_weights_compound(compound, mass_numbers)
                msp_values = {}

                for element in compound:
                    msp_values[element] = self.get_msp(sent_ion, element, energy, data_folder)

                msp_target = self.calculate_msp_target_compound(compound, weights, msp_values)
                
                msp_water = self.calculate_msp_water(data_folder, sent_ion, energy)
                
                PRSP_target = msp_target / msp_water
                
                sigma_target = self.calculate_sigma_target(msp_target, weights, mass_numbers)

                all_elements = [
                    "Ag","Au","Br","Ce","Cs","Eu","Gd","Hf","In","La","Mn","Nb","O","Pd","Rb",
                    "S","Si","Ta","Ti","W","Zn","Al","B","C","Cl","Cu","F","Ge","Hg","Ir",
                    "Li","Mo","Nd","Os","Pm","Re","Sb","Sm","Tb","Tl","Xe","Zr","Ar","Ba",
                    "Ca","Co","Dy","Fe","H","Ho","K","Lu","N","Ne","P","Pr","Rh","Sc","Sn",
                    "Tc","Tm","Y","As","Be","Cd","Cr","Er","Ga","He","I","Kr","Mg","Na","Ni",
                    "Pb","Pt","Ru","Se","Sr","Te","V","Yb"
                ]

                sigma_values = self.calculate_elements_sigma(sent_ion, all_elements, energy, mass_numbers, data_folder, results_folder)

                sigma_1, sigma_2, Z_1, Z_2 = self.find_sigma_bounds(sigma_target, sigma_values, atomic_numbers)

                Z_eff = self.calculate_z_eff(sigma_target, sigma_1, sigma_2, Z_1, Z_2)

                A_average = self.calculate_a_average(weights, mass_numbers)

                N_e = self.calculate_n_e(Z_eff, A_average)

                results.append({
                    'energy': energy,
                    'msp_target': msp_target,
                    'sigma_target': sigma_target,
                    'Z_eff': Z_eff,
                    'N_e': N_e,
                    'WRSP_target': PRSP_target
                })

                row_count = self.ui.tableWidget_Results.rowCount()
                self.ui.tableWidget_Results.insertRow(row_count)
                self.ui.tableWidget_Results.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(energy)))
                self.ui.tableWidget_Results.setItem(row_count, 1, QtWidgets.QTableWidgetItem(f"{msp_target}"))
                self.ui.tableWidget_Results.setItem(row_count, 2, QtWidgets.QTableWidgetItem(f"{sigma_target}"))
                self.ui.tableWidget_Results.setItem(row_count, 3, QtWidgets.QTableWidgetItem(f"{Z_eff}"))
                self.ui.tableWidget_Results.setItem(row_count, 4, QtWidgets.QTableWidgetItem(f"{N_e}"))
                self.ui.tableWidget_Results.setItem(row_count, 5, QtWidgets.QTableWidgetItem(f"{PRSP_target}"))

            except Exception as e:
                self.ui.label_2.setText(f"Error processing energy {energy} MeV: {e}")
                results.append({
                    'energy': energy,
                    'msp_target': None,  
                    'sigma_target': None,
                    'Z_eff': None,
                    'N_e': None,
                    'WRSP_target': None
                })

        self.ui.tableWidget_Chemical_Formula.setRowCount(0)
        row_count = self.ui.tableWidget_Chemical_Formula.rowCount()
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(target_formula)))

        self.ui.label_2.setText(f"All energy calculations completed.")


   # MSP COMPOSITION ALL
    def process_all_energies_composition(self, sent_ion, target_formula, atomic_numbers, mass_numbers, data_folder, results_folder):

        composition = self.parse_composition(target_formula)

        first_element = next(iter(composition))
        sention_folder = os.path.join(data_folder, f"{sent_ion}-data")
        first_element_csv = os.path.join(sention_folder, f"{first_element}.csv")

        if not os.path.exists(first_element_csv):
            raise FileNotFoundError(f"{first_element_csv} does not exist.")

        df_first = pd.read_csv(first_element_csv, header=None, names=['Energy', 'MSP', 'Projected Range', 'Longitudinal Straggling', 'Lateral Straggling'])
        energies = df_first['Energy'].unique()

        results = []

        self.ui.tableWidget_Results.setRowCount(0)
        self.ui.tableWidget_Results.setColumnCount(6) 
        self.ui.tableWidget_Results.setHorizontalHeaderLabels(["Energy", "MSP Target", "Sigma Target", "Z_eff", "N_e", "WRSP"])

        for energy in sorted(energies):
            try:
                weights = self.calculate_weights_composition(composition)
                msp_values = {}

                for element in composition:
                    msp_values[element] = self.get_msp(sent_ion, element, energy, data_folder)

                msp_target = self.calculate_msp_target_composition(composition, weights, msp_values)

                msp_water = self.calculate_msp_water(data_folder, sent_ion, energy)
                
                PRSP_target = msp_target / msp_water

                sigma_target = self.calculate_sigma_target(msp_target, weights, mass_numbers)

                all_elements = [
                    "Ag", "Au", "Br", "Ce", "Cs", "Eu", "Gd", "Hf", "In", "La", "Mn", "Nb", "O", "Pd", "Rb",
                    "S", "Si", "Ta", "Ti", "W", "Zn", "Al", "B", "C", "Cl", "Cu", "F", "Ge", "Hg", "Ir",
                    "Li", "Mo", "Nd", "Os", "Pm", "Re", "Sb", "Sm", "Tb", "Tl", "Xe", "Zr", "Ar", "Ba",
                    "Ca", "Co", "Dy", "Fe", "H", "Ho", "K", "Lu", "N", "Ne", "P", "Pr", "Rh", "Sc", "Sn",
                    "Tc", "Tm", "Y", "As", "Be", "Cd", "Cr", "Er", "Ga", "He", "I", "Kr", "Mg", "Na", "Ni",
                    "Pb", "Pt", "Ru", "Se", "Sr", "Te", "V", "Yb"
                ]

                sigma_values = self.calculate_elements_sigma(sent_ion, all_elements, energy, mass_numbers, data_folder, results_folder)

                sigma_1, sigma_2, Z_1, Z_2 = self.find_sigma_bounds(sigma_target, sigma_values, atomic_numbers)

                Z_eff = self.calculate_z_eff(sigma_target, sigma_1, sigma_2, Z_1, Z_2)

                A_average = self.calculate_a_average(weights, mass_numbers)

                N_e = self.calculate_n_e(Z_eff, A_average)

                results.append({
                    'energy': energy,
                    'msp_target': msp_target,
                    'sigma_target': sigma_target,
                    'Z_eff': Z_eff,
                    'N_e': N_e,
                    'WRSP_target': PRSP_target
                })

                row_count = self.ui.tableWidget_Results.rowCount()
                self.ui.tableWidget_Results.insertRow(row_count)
                self.ui.tableWidget_Results.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(energy)))
                self.ui.tableWidget_Results.setItem(row_count, 1, QtWidgets.QTableWidgetItem(f"{msp_target}"))
                self.ui.tableWidget_Results.setItem(row_count, 2, QtWidgets.QTableWidgetItem(f"{sigma_target}"))
                self.ui.tableWidget_Results.setItem(row_count, 3, QtWidgets.QTableWidgetItem(f"{Z_eff}"))
                self.ui.tableWidget_Results.setItem(row_count, 4, QtWidgets.QTableWidgetItem(f"{N_e}"))
                self.ui.tableWidget_Results.setItem(row_count, 5, QtWidgets.QTableWidgetItem(f"{PRSP_target}")) 

            except Exception as e:
                self.ui.label_2.setText(f"Error processing energy {energy} MeV: {e}")
                results.append({
                    'energy': energy,
                    'msp_target': None, 
                    'sigma_target': None,
                    'Z_eff': None,
                    'N_e': None,
                    'WRSP_target': None
                })

        self.ui.tableWidget_Chemical_Formula.setRowCount(0)
        row_count = self.ui.tableWidget_Chemical_Formula.rowCount()
        self.ui.tableWidget_Chemical_Formula.insertRow(row_count)
        self.ui.tableWidget_Chemical_Formula.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(target_formula)))

        self.ui.label_2.setText(f"All energy calculations completed.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
