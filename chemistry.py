# -----------------Exceeding the Requirements----------
# I added a dictionary that contains known chemical formulas and their names as the example shown

from formula import parse_formula
import sys
def make_periodic_table():
    periodic_table_dict = {
    # symbol: [name, atomic_mass]
    "Ac": ["Actinium", 227],
    "Ag": ["Silver", 107.8682],
    "Al": ["Aluminum", 26.9815386],
    "Ar": ["Argon", 39.948],
    "As": ["Arsenic", 74.9216],
    "At": ["Astatine", 210],
    "Au": ["Gold", 196.966569],
    "B": ["Boron", 10.811],
    "Ba": ["Barium", 137.327],
    "Be": ["Beryllium", 9.012182],
    "Bi": ["Bismuth", 208.9804],
    "Br": ["Bromine", 79.904],
    "C": ["Carbon", 12.0107],
    "Ca": ["Calcium", 40.078],
    "Cd": ["Cadmium", 112.411],
    "Ce": ["Cerium", 140.116],
    "Cl": ["Chlorine", 35.453],
    "Co": ["Cobalt", 58.933195],
    "Cr": ["Chromium", 51.9961],
    "Cs": ["Cesium", 132.9054519],
    "Cu": ["Copper", 63.546],
    "Dy": ["Dysprosium", 162.5],
    "Er": ["Erbium", 167.259],
    "Eu": ["Europium", 151.964],
    "F": ["Fluorine", 18.9984032],
    "Fe": ["Iron", 55.845],
    "Fr": ["Francium", 223],
    "Ga": ["Gallium", 69.723],
    "Gd": ["Gadolinium", 157.25],
    "Ge": ["Germanium", 72.64],
    "H": ["Hydrogen", 1.00794],
    "He": ["Helium", 4.002602],
    "Hf": ["Hafnium", 178.49],
    "Hg": ["Mercury", 200.59],
    "Ho": ["Holmium", 164.93032],
    "I": ["Iodine", 126.90447],
    "In": ["Indium", 114.818],
    "Ir": ["Iridium", 192.217],
    "K": ["Potassium", 39.0983],
    "Kr": ["Krypton", 83.798],
    "La": ["Lanthanum", 138.90547],
    "Li": ["Lithium", 6.941],
    "Lu": ["Lutetium", 174.9668],
    "Mg": ["Magnesium", 24.305],
    "Mn": ["Manganese", 54.938045],
    "Mo": ["Molybdenum", 95.96],
    "N": ["Nitrogen", 14.0067],
    "Na": ["Sodium", 22.98976928],
    "Nb": ["Niobium", 92.90638],
    "Nd": ["Neodymium", 144.242],
    "Ne": ["Neon", 20.1797],
    "Ni": ["Nickel", 58.6934],
    "Np": ["Neptunium", 237],
    "O": ["Oxygen", 15.9994],
    "Os": ["Osmium", 190.23],
    "P": ["Phosphorus", 30.973762],
    "Pa": ["Protactinium", 231.03588],
    "Pb": ["Lead", 207.2],
    "Pd": ["Palladium", 106.42],
    "Pm": ["Promethium", 145],
    "Po": ["Polonium", 209],
    "Pr": ["Praseodymium", 140.90765],
    "Pt": ["Platinum", 195.084],
    "Pu": ["Plutonium", 244],
    "Ra": ["Radium", 226],
    "Rb": ["Rubidium", 85.4678],
    "Re": ["Rhenium", 186.207],
    "Rh": ["Rhodium", 102.9055],
    "Rn": ["Radon", 222],
    "Ru": ["Ruthenium", 101.07],
    "S": ["Sulfur", 32.065],
    "Sb": ["Antimony", 121.76],
    "Sc": ["Scandium", 44.955912],
    "Se": ["Selenium", 78.96],
    "Si": ["Silicon", 28.0855],
    "Sm": ["Samarium", 150.36],
    "Sn": ["Tin", 118.71],
    "Sr": ["Strontium", 87.62],
    "Ta": ["Tantalum", 180.94788],
    "Tb": ["Terbium", 158.92535],
    "Tc": ["Technetium", 98],
    "Te": ["Tellurium", 127.6],
    "Th": ["Thorium", 232.03806],
    "Ti": ["Titanium", 47.867],
    "Tl": ["Thallium", 204.3833],
    "Tm": ["Thulium", 168.93421],
    "U": ["Uranium", 238.02891],
    "V": ["Vanadium", 50.9415],
    "W": ["Tungsten", 183.84],
    "Xe": ["Xenon", 131.293],
    "Y": ["Yttrium", 88.90585],
    "Yb": ["Ytterbium", 173.054],
    "Zn": ["Zinc", 65.38],
    "Zr": ["Zirconium", 91.224]
}
    return(periodic_table_dict)

# -----------------Exceeding the Requirements----------
known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }
#--------------Function Creation---------------

# -----------------Exceeding the Requirements----------
def get_formula_name(formula, known_molecules_dict):
    
    try:
        sample_name_formula = known_molecules_dict[formula]
    except KeyError:
        sample_name_formula = "None exsistent formula name"


    return sample_name_formula



def main():

    # Verificar si pytest está ejecutando el script
    if not any('pytest' in arg for arg in sys.argv):
        user_formual  = input("Please insert formula: ")
    
        user_mass_grams = float(input("Enter the mass in grams of the sample: "))

    else:
        # En pruebas, podrías usar un valor predeterminado o saltar esta parte
        print("No se solicitará la fórmula durante las pruebas.")
        user_formual = "H2O"  # Ejemplo de fórmula predeterminada para pruebas
        user_mass_grams = 18.015

    dict_periodic_table = make_periodic_table()
    formula_and_list = parse_formula(user_formual, dict_periodic_table)
    molar_mass_calculation = compute_molar_mass(formula_and_list, dict_periodic_table)
    number_of_moles = user_mass_grams/molar_mass_calculation
    print(f"{round(molar_mass_calculation, 5)} grams/moles")
    print(f"{round(number_of_moles, 5)} moles")
    
    print(get_formula_name(user_formual, known_molecules_dict))













# print(formula_and_list)

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1



def compute_molar_mass(symbol_quantity_list, periodic_table_dict):

    molar_mass=0

    for one_symbol_quantity_list in symbol_quantity_list:
        symbol = one_symbol_quantity_list[0]
        symbol_atomic_mass =  one_symbol_quantity_list[1]
        atomic_table_mass = periodic_table_dict[symbol][1]
        calculation_atomic_mass = symbol_atomic_mass * atomic_table_mass
        molar_mass += calculation_atomic_mass
        
    
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    # Return the total molar mass.
    return molar_mass

# compute_molar_mass(formula_and_list, dict_periodic_table)







main()



