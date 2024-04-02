import os
import sqlite3
import sys
import webbrowser

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from Project import Ui_MainWindow
from Search import Search_Form
from Info import Info_Form
from Additional_info import Additional_Form
from Pointer import Pointer_Form
from Theme import Theme_Form


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Search.clicked.connect(self.open_search)
        self.pushButton_2.clicked.connect(self.open_pointer)
        self.Hydrogenium.clicked.connect(self.open_hydrogenium)
        self.Helium.clicked.connect(self.open_helium)
        self.Lithium.clicked.connect(self.open_lithium)
        self.Beryllium.clicked.connect(self.open_beryllium)
        self.Borum.clicked.connect(self.open_borum)
        self.Carboneum.clicked.connect(self.open_carboneum)
        self.Nitrogenium.clicked.connect(self.open_nitrogenium)
        self.Oxygenium.clicked.connect(self.open_oxygenium)
        self.Fluorum.clicked.connect(self.open_fluorum)
        self.Neon.clicked.connect(self.open_neon)
        self.Natrium.clicked.connect(self.open_natrium)
        self.Magnesium.clicked.connect(self.open_magnesium)
        self.Aluminium.clicked.connect(self.open_aluminium)
        self.Silicium.clicked.connect(self.open_silicium)
        self.Phosphorus.clicked.connect(self.open_phosphorus)
        self.Sulfur.clicked.connect(self.open_sulfur)
        self.Chlorum.clicked.connect(self.open_chlorum)
        self.Argon.clicked.connect(self.open_argon)
        self.Kalium.clicked.connect(self.open_kalium)
        self.Calcium.clicked.connect(self.open_calcium)
        self.Scandium.clicked.connect(self.open_scandium)
        self.Titanium.clicked.connect(self.open_titanium)
        self.Vanadium.clicked.connect(self.open_vanadium)
        self.Chromium.clicked.connect(self.open_chromium)
        self.Manganesium.clicked.connect(self.open_manganesium)
        self.Ferrum.clicked.connect(self.open_ferrum)
        self.Cobaltum.clicked.connect(self.open_cobaltum)
        self.Niccolum.clicked.connect(self.open_niccolum)
        self.Cuprum.clicked.connect(self.open_cuprum)
        self.Zincum.clicked.connect(self.open_zincum)
        self.Gallium.clicked.connect(self.open_gallium)
        self.Germanium.clicked.connect(self.open_germanium)
        self.Arsenicum.clicked.connect(self.open_arsenicum)
        self.Selenium.clicked.connect(self.open_selenium)
        self.Bromum.clicked.connect(self.open_bromum)
        self.Krypton.clicked.connect(self.open_krypton)
        self.Rubidium.clicked.connect(self.open_rubidium)
        self.Strontium.clicked.connect(self.open_strontium)
        self.Yttrium.clicked.connect(self.open_yttrium)
        self.Zirconium.clicked.connect(self.open_zirconium)
        self.Niobium.clicked.connect(self.open_niobium)
        self.Molybdaenum.clicked.connect(self.open_molybdaenum)
        self.Technetium.clicked.connect(self.open_technetium)
        self.Ruthenium.clicked.connect(self.open_ruthenium)
        self.Rhodium.clicked.connect(self.open_rhodium)
        self.Palladium.clicked.connect(self.open_palladium)
        self.Argentum.clicked.connect(self.open_argentum)
        self.Cadmium.clicked.connect(self.open_cadmium)
        self.Indium.clicked.connect(self.open_indium)
        self.Stannum.clicked.connect(self.open_stannum)
        self.Stibium.clicked.connect(self.open_stibium)
        self.Tellurium.clicked.connect(self.open_tellurium)
        self.Iodium.clicked.connect(self.open_iodium)
        self.Xenon.clicked.connect(self.open_xenon)
        self.Caesium.clicked.connect(self.open_caesium)
        self.Barium.clicked.connect(self.open_barium)
        self.Lanthanum.clicked.connect(self.open_lanthanum)
        self.Cerium.clicked.connect(self.open_cerium)
        self.Praseodymium.clicked.connect(self.open_praseodymium)
        self.Neodymium.clicked.connect(self.open_neodymium)
        self.Promethium.clicked.connect(self.open_promethium)
        self.Samarium.clicked.connect(self.open_samarium)
        self.Europium.clicked.connect(self.open_europium)
        self.Gadolinium.clicked.connect(self.open_gadolinium)
        self.Terbium.clicked.connect(self.open_terbium)
        self.Dysprosium.clicked.connect(self.open_dysprosium)
        self.Holmium.clicked.connect(self.open_holmium)
        self.Erbium.clicked.connect(self.open_erbium)
        self.Thulium.clicked.connect(self.open_thulium)
        self.Ytterbium.clicked.connect(self.open_ytterbium)
        self.Lutetium.clicked.connect(self.open_lutetium)
        self.Hafnium.clicked.connect(self.open_hafnium)
        self.Tantalum.clicked.connect(self.open_tantalum)
        self.Wolframium.clicked.connect(self.open_wolframium)
        self.Rhenium.clicked.connect(self.open_rhenium)
        self.Osmium.clicked.connect(self.open_osmium)
        self.Iridium.clicked.connect(self.open_iridium)
        self.Platinum.clicked.connect(self.open_platinum)
        self.Aurum.clicked.connect(self.open_aurum)
        self.Hydrargyrum.clicked.connect(self.open_hydrargyrum)
        self.Thallium.clicked.connect(self.open_thallium)
        self.Plumbum.clicked.connect(self.open_plumbum)
        self.Bismuthum.clicked.connect(self.open_bismuthum)
        self.Polonium.clicked.connect(self.open_polonium)
        self.Astatum.clicked.connect(self.open_astatum)
        self.Radon.clicked.connect(self.open_radon)
        self.Francium.clicked.connect(self.open_francium)
        self.Radium.clicked.connect(self.open_radium)
        self.Actinium.clicked.connect(self.open_actinium)
        self.Thorium.clicked.connect(self.open_thorium)
        self.Protactinium.clicked.connect(self.open_protactinium)
        self.Uranium.clicked.connect(self.open_uranium)
        self.Neptunium.clicked.connect(self.open_neptunium)
        self.Plutonium.clicked.connect(self.open_plutonium)
        self.Americium.clicked.connect(self.open_americium)
        self.Curium.clicked.connect(self.open_curium)
        self.Berkelium.clicked.connect(self.open_berkelium)
        self.Californium.clicked.connect(self.open_californium)
        self.Einsteinium.clicked.connect(self.open_einsteinium)
        self.Fermium.clicked.connect(self.open_fermium)
        self.Mendelevium.clicked.connect(self.open_mendelevium)
        self.Nobelium.clicked.connect(self.open_nobelium)
        self.Lawrencium.clicked.connect(self.open_lawrencium)
        self.Rutherfordium.clicked.connect(self.open_rutherfordium)
        self.Dubnium.clicked.connect(self.open_dubnium)
        self.Seaborgium.clicked.connect(self.open_seaborgium)
        self.Bohrium.clicked.connect(self.open_bohrium)
        self.Hassium.clicked.connect(self.open_hassium)
        self.Meitnerium.clicked.connect(self.open_meitnerium)
        self.Darmstadtium.clicked.connect(self.open_darmstadtium)
        self.Roentgenium.clicked.connect(self.open_roentgenium)
        self.Copernicium.clicked.connect(self.open_copernicium)
        self.Nihonium.clicked.connect(self.open_nihonium)
        self.Flerovium.clicked.connect(self.open_flerovium)
        self.Moscovium.clicked.connect(self.open_moscovium)
        self.Livermorium.clicked.connect(self.open_livermorium)
        self.Tennessine.clicked.connect(self.open_tennessine)
        self.Oganesson.clicked.connect(self.open_oganesson)

    def open_search(self):
        self.search = SearchElements()
        self.search.show()

    def open_pointer(self):
        self.pointer = Pointer()
        self.pointer.show()

    def open_hydrogenium(self):
        self.Hydrogenium = ElementsInfo()
        self.Hydrogenium.show()

    def open_helium(self):
        self.Helium = ElementsInfo()
        self.Helium.show()

    def open_lithium(self):
        self.Lithium = ElementsInfo()
        self.Lithium.show()

    def open_beryllium(self):
        self.Beryllium = ElementsInfo()
        self.Beryllium.show()

    def open_borum(self):
        self.Borum = ElementsInfo()
        self.Borum.show()

    def open_carboneum(self):
        self.Carboneum = ElementsInfo()
        self.Carboneum.show()

    def open_nitrogenium(self):
        self.Nitrogenium = ElementsInfo()
        self.Nitrogenium.show()

    def open_oxygenium(self):
        self.Oxygenium = ElementsInfo()
        self.Oxygenium.show()

    def open_fluorum(self):
        self.Fluorum = ElementsInfo()
        self.Fluorum.show()

    def open_neon(self):
        self.Neon = ElementsInfo()
        self.Neon.show()

    def open_natrium(self):
        self.Natrium = ElementsInfo()
        self.Natrium.show()

    def open_magnesium(self):
        self.Magnesium = ElementsInfo()
        self.Magnesium.show()

    def open_aluminium(self):
        self.Aluminium = ElementsInfo()
        self.Aluminium.show()

    def open_silicium(self):
        self.Silicium = ElementsInfo()
        self.Silicium.show()

    def open_phosphorus(self):
        self.Phosphorus = ElementsInfo()
        self.Phosphorus.show()

    def open_sulfur(self):
        self.Sulfur = ElementsInfo()
        self.Sulfur.show()

    def open_chlorum(self):
        self.Chlorum = ElementsInfo()
        self.Chlorum.show()

    def open_argon(self):
        self.Argon = ElementsInfo()
        self.Argon.show()

    def open_kalium(self):
        self.Kalium = ElementsInfo()
        self.Kalium.show()

    def open_calcium(self):
        self.Calcium = ElementsInfo()
        self.Calcium.show()

    def open_scandium(self):
        self.Scandium = ElementsInfo()
        self.Scandium.show()

    def open_titanium(self):
        self.Titanium = ElementsInfo()
        self.Titanium.show()

    def open_vanadium(self):
        self.Vanadium = ElementsInfo()
        self.Vanadium.show()

    def open_chromium(self):
        self.Chromium = ElementsInfo()
        self.Chromium.show()

    def open_manganesium(self):
        self.Manganesium = ElementsInfo()
        self.Manganesium.show()

    def open_ferrum(self):
        self.Ferrum = ElementsInfo()
        self.Ferrum.show()

    def open_cobaltum(self):
        self.Cobaltum = ElementsInfo()
        self.Cobaltum.show()

    def open_niccolum(self):
        self.Niccolum = ElementsInfo()
        self.Niccolum.show()

    def open_cuprum(self):
        self.Cuprum = ElementsInfo()
        self.Cuprum.show()

    def open_zincum(self):
        self.Zincum = ElementsInfo()
        self.Zincum.show()

    def open_gallium(self):
        self.Gallium = ElementsInfo()
        self.Gallium.show()

    def open_germanium(self):
        self.Germanium = ElementsInfo()
        self.Germanium.show()

    def open_arsenicum(self):
        self.Arsenicum = ElementsInfo()
        self.Arsenicum.show()

    def open_selenium(self):
        self.Selenium = ElementsInfo()
        self.Selenium.show()

    def open_bromum(self):
        self.Bromum = ElementsInfo()
        self.Bromum.show()

    def open_krypton(self):
        self.Krypton = ElementsInfo()
        self.Krypton.show()

    def open_rubidium(self):
        self.Rubidium = ElementsInfo()
        self.Rubidium.show()

    def open_strontium(self):
        self.Strontium = ElementsInfo()
        self.Strontium.show()

    def open_yttrium(self):
        self.Yttrium = ElementsInfo()
        self.Yttrium.show()

    def open_zirconium(self):
        self.Zirconium = ElementsInfo()
        self.Zirconium.show()

    def open_niobium(self):
        self.Niobium = ElementsInfo()
        self.Niobium.show()

    def open_molybdaenum(self):
        self.Molybdaenum = ElementsInfo()
        self.Molybdaenum.show()

    def open_technetium(self):
        self.Technetium = ElementsInfo()
        self.Technetium.show()

    def open_ruthenium(self):
        self.Ruthenium = ElementsInfo()
        self.Ruthenium.show()

    def open_rhodium(self):
        self.Rhodium = ElementsInfo()
        self.Rhodium.show()

    def open_palladium(self):
        self.Palladium = ElementsInfo()
        self.Palladium.show()

    def open_argentum(self):
        self.Argentum = ElementsInfo()
        self.Argentum.show()

    def open_cadmium(self):
        self.Cadmium = ElementsInfo()
        self.Cadmium.show()

    def open_indium(self):
        self.Indium = ElementsInfo()
        self.Indium.show()

    def open_stannum(self):
        self.Stannum = ElementsInfo()
        self.Stannum.show()

    def open_stibium(self):
        self.Stibium = ElementsInfo()
        self.Stibium.show()

    def open_tellurium(self):
        self.Tellurium = ElementsInfo()
        self.Tellurium.show()

    def open_iodium(self):
        self.Iodium = ElementsInfo()
        self.Iodium.show()

    def open_xenon(self):
        self.Xenon = ElementsInfo()
        self.Xenon.show()

    def open_caesium(self):
        self.Caesium = ElementsInfo()
        self.Caesium.show()

    def open_barium(self):
        self.Barium = ElementsInfo()
        self.Barium.show()

    def open_lanthanum(self):
        self.Lanthanum = ElementsInfo()
        self.Lanthanum.show()

    def open_cerium(self):
        self.Cerium = ElementsInfo()
        self.Cerium.show()

    def open_praseodymium(self):
        self.Praseodymium = ElementsInfo()
        self.Praseodymium.show()

    def open_neodymium(self):
        self.Neodymium = ElementsInfo()
        self.Neodymium.show()

    def open_promethium(self):
        self.Promethium = ElementsInfo()
        self.Promethium.show()

    def open_samarium(self):
        self.Samarium = ElementsInfo()
        self.Samarium.show()

    def open_europium(self):
        self.Europium = ElementsInfo()
        self.Europium.show()

    def open_gadolinium(self):
        self.Gadolinium = ElementsInfo()
        self.Gadolinium.show()

    def open_terbium(self):
        self.Terbium = ElementsInfo()
        self.Terbium.show()

    def open_dysprosium(self):
        self.Dysprosium = ElementsInfo()
        self.Dysprosium.show()

    def open_holmium(self):
        self.Holmium = ElementsInfo()
        self.Holmium.show()

    def open_erbium(self):
        self.Erbium = ElementsInfo()
        self.Erbium.show()

    def open_thulium(self):
        self.Thulium = ElementsInfo()
        self.Thulium.show()

    def open_ytterbium(self):
        self.Ytterbium = ElementsInfo()
        self.Ytterbium.show()

    def open_lutetium(self):
        self.Lutetium = ElementsInfo()
        self.Lutetium.show()

    def open_hafnium(self):
        self.Hafnium = ElementsInfo()
        self.Hafnium.show()

    def open_tantalum(self):
        self.Tantalum = ElementsInfo()
        self.Tantalum.show()

    def open_wolframium(self):
        self.Wolframium = ElementsInfo()
        self.Wolframium.show()

    def open_rhenium(self):
        self.Rhenium = ElementsInfo()
        self.Rhenium.show()

    def open_osmium(self):
        self.Osmium = ElementsInfo()
        self.Osmium.show()

    def open_iridium(self):
        self.Iridium = ElementsInfo()
        self.Iridium.show()

    def open_platinum(self):
        self.Platinum = ElementsInfo()
        self.Platinum.show()

    def open_aurum(self):
        self.Aurum = ElementsInfo()
        self.Aurum.show()

    def open_hydrargyrum(self):
        self.Hydrargyrum = ElementsInfo()
        self.Hydrargyrum.show()

    def open_thallium(self):
        self.Thallium = ElementsInfo()
        self.Thallium.show()

    def open_plumbum(self):
        self.Plumbum = ElementsInfo()
        self.Plumbum.show()

    def open_bismuthum(self):
        self.Bismuthum = ElementsInfo()
        self.Bismuthum.show()

    def open_polonium(self):
        self.Polonium = ElementsInfo()
        self.Polonium.show()

    def open_astatum(self):
        self.Astatum = ElementsInfo()
        self.Astatum.show()

    def open_radon(self):
        self.Radon = ElementsInfo()
        self.Radon.show()

    def open_francium(self):
        self.Francium = ElementsInfo()
        self.Francium.show()

    def open_radium(self):
        self.Radium = ElementsInfo()
        self.Radium.show()

    def open_actinium(self):
        self.Actinium = ElementsInfo()
        self.Actinium.show()

    def open_thorium(self):
        self.Thorium = ElementsInfo()
        self.Thorium.show()

    def open_protactinium(self):
        self.Protactinium = ElementsInfo()
        self.Protactinium.show()

    def open_uranium(self):
        self.Uranium = ElementsInfo()
        self.Uranium.show()

    def open_neptunium(self):
        self.Neptunium = ElementsInfo()
        self.Neptunium.show()

    def open_plutonium(self):
        self.Plutonium = ElementsInfo()
        self.Plutonium.show()

    def open_americium(self):
        self.Americium = ElementsInfo()
        self.Americium.show()

    def open_curium(self):
        self.Curium = ElementsInfo()
        self.Curium.show()

    def open_berkelium(self):
        self.Berkelium = ElementsInfo()
        self.Berkelium.show()

    def open_californium(self):
        self.Californium = ElementsInfo()
        self.Californium.show()

    def open_einsteinium(self):
        self.Einsteinium = ElementsInfo()
        self.Einsteinium.show()

    def open_fermium(self):
        self.Fermium = ElementsInfo()
        self.Fermium.show()

    def open_mendelevium(self):
        self.Mendelevium = ElementsInfo()
        self.Mendelevium.show()

    def open_nobelium(self):
        self.Nobelium = ElementsInfo()
        self.Nobelium.show()

    def open_lawrencium(self):
        self.Lawrencium = ElementsInfo()
        self.Lawrencium.show()

    def open_rutherfordium(self):
        self.Rutherfordium = ElementsInfo()
        self.Rutherfordium.show()

    def open_dubnium(self):
        self.Dubnium = ElementsInfo()
        self.Dubnium.show()

    def open_seaborgium(self):
        self.Seaborgium = ElementsInfo()
        self.Seaborgium.show()

    def open_bohrium(self):
        self.Bohrium = ElementsInfo()
        self.Bohrium.show()

    def open_hassium(self):
        self.Hassium = ElementsInfo()
        self.Hassium.show()

    def open_meitnerium(self):
        self.Meitnerium = ElementsInfo()
        self.Meitnerium.show()

    def open_darmstadtium(self):
        self.Darmstadtium = ElementsInfo()
        self.Darmstadtium.show()

    def open_roentgenium(self):
        self.Roentgenium = ElementsInfo()
        self.Roentgenium.show()

    def open_copernicium(self):
        self.Copernicium = ElementsInfo()
        self.Copernicium.show()

    def open_nihonium(self):
        self.Nihonium = ElementsInfo()
        self.Nihonium.show()

    def open_flerovium(self):
        self.Flerovium = ElementsInfo()
        self.Flerovium.show()

    def open_moscovium(self):
        self.Moscovium = ElementsInfo()
        self.Moscovium.show()

    def open_livermorium(self):
        self.Livermorium = ElementsInfo()
        self.Livermorium.show()

    def open_tennessine(self):
        self.Tennessine = ElementsInfo()
        self.Tennessine.show()

    def open_oganesson(self):
        self.Oganesson = ElementsInfo()
        self.Oganesson.show()


requests = {
    'Порядковый номер': 'Порядковый номер',
    'Название': 'Название',
    'Латинское название': 'Латинское название',
    'Символ': 'Символ'
}


class SearchElements(QWidget, Search_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.variants.addItems(requests)
        self.queryButton.clicked.connect(self.search)
        self.con = sqlite3.connect('Elements_db')

    def search(self):
        parameters = self.request.text()
        query = ("SELECT * FROM Элементы WHERE \""
                 + requests[self.variants.currentText()] + "\" = ?")
        try:
            result = self.con.cursor().execute(query, (parameters,)).fetchone()
            if result:
                self.Error.setText('')
                for i, w in enumerate((self.Number, self.Symbol, self.LatName, self.Name,
                                       self.Type, self.Aggregate)):
                    w.setText(str(result[i]))
            else:
                self.Error.setText('Ничего не найдено')
        except sqlite3.Error:
            self.Error.setText('Неправильный запрос')


class ElementsInfo(QWidget, Info_Form):
    def __init__(self, name=None):
        super().__init__()
        self.setupUi(self)
        self.add_info.clicked.connect(self.open_add_info)
        if name is not None:
            self.name = name
        else:
            self.name = self.sender().objectName()
        if self.name:
            self.el_name_label.setText(self.name)
            text = open(f'Elements and stuff/Elements/{self.name}.txt', encoding="utf-8").read()
            self.info.setText(text)
            if (os.path.isfile(f'Elements and stuff/Physical properties/{self.name}.txt') and
                    os.path.isfile(f'Elements and stuff/Chemical properties/{self.name}.txt')):
                phys_text = open(f'Elements and stuff/Physical properties/{self.name}.txt', encoding="utf-8").read()
                chem_text = open(f'Elements and stuff/Chemical properties/{self.name}.txt', encoding="utf-8").read()
                self.physics.setText(phys_text)
                self.chemistry.setText(chem_text)
            else:
                pass
        else:
            self.name = self.sender().objectName()

    def open_add_info(self):
        self.add = AdditionalInfo(self.name)
        self.close()
        self.add.show()


class AdditionalInfo(QWidget, Additional_Form):
    def __init__(self, name):
        super(AdditionalInfo, self).__init__()
        self.setupUi(self)
        self.name = name
        self.back.clicked.connect(self.comeback)
        self.label.setText(f'Дополнительная информация ({self.name})')
        if self.name:
            text = open(f'Elements and stuff/Additional_elements/add_{self.name}.txt',
                        encoding="utf-8").read().split('\n')
            if len(text) == 9:
                self.PerGroup.setText(text[0])
                self.Weight.setText(text[1])
                self.Density.setText(text[2])
                self.Melting.setText(text[3])
                self.Boiling.setText(text[4])
                self.Year.setText(text[5])
                self.Discoverer.setText(text[6])
                self.Energy.setText(text[7])
                self.Section.setText(self.name)
                self.Section.clicked.connect(lambda: webbrowser.open(text[8]))
            else:
                text = open(f'Elements and stuff/Additional_elements/add_{self.name}.txt',
                            encoding="utf-8").read().split('\t')
                self.PerGroup.setText(text[0])
                self.Weight.setText(text[1])
                self.Density.setText(text[2])
                self.Melting.setText(text[3])
                self.Boiling.setText(text[4])
                self.Year.setText(text[5])
                self.Discoverer.setText(text[6])
        else:
            self.name = ElementsInfo.name

    def comeback(self):
        self.info = ElementsInfo(self.name)
        self.close()
        self.info.show()


class Pointer(QWidget, Pointer_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first.clicked.connect(self.open_theme)
        self.second.clicked.connect(self.open_theme)
        self.third.clicked.connect(self.open_theme)
        self.fourth.clicked.connect(self.open_theme)
        self.fifth.clicked.connect(self.open_theme)
        self.sixth.clicked.connect(self.open_theme)

    def open_theme(self):
        self.theme = Theme()
        self.close()
        self.theme.show()


class Theme(QWidget, Theme_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.comeback)
        self.name = self.sender().objectName()
        if self.name:
            if self.name == 'first':
                text = open('Themes/Алканы.txt', encoding='utf-8').read()
                self.label.setText('Алканы')
                self.theme_info.setText(text)
            elif self.name == 'second':
                text = open('Themes/Алкены.txt', encoding='utf-8').read()
                self.label.setText('Алкены')
                self.theme_info.setText(text)
            elif self.name == 'third':
                text = open('Themes/Нефть.txt', encoding='utf-8').read()
                self.label.setText('Нефть')
                self.theme_info.setText(text)
            elif self.name == 'fourth':
                text = open('Themes/ОЧ.txt', encoding='utf-8').read()
                self.label.setText('Октановое число')
                self.theme_info.setText(text)
            elif self.name == 'fifth':
                text = open('Themes/Крекинг.txt', encoding='utf-8').read()
                self.label.setText('Крекинг нефти')
                self.theme_info.setText(text)
            elif self.name == 'sixth':
                text = open('Themes/Риформинг.txt', encoding='utf-8').read()
                self.label.setText('Каталитический риформинг нефти')
                self.theme_info.setText(text)
        else:
            self.name = Pointer.name

    def comeback(self):
        self.pointer = Pointer()
        self.close()
        self.pointer.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Main()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
