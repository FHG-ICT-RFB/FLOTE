import math
from numpy import log

def SVF(edt1, edt2, Val1, Val2) :

    ###########################
    ######### ENERGY ##########
    ###########################

    # G SPACE ################################################################

    ### KNOWN INFO ### SoC min

    if edt1 == 'SoC_min' :
        eG4 = Val1
    elif edt2 == 'SoC_min' :
        eG4 = Val2
    else :
        eG4=0.05

    ### KNOWN INFO ### SoC max
    if edt1 == 'SoC_max' :
        eG5 = Val1
    elif edt2 == 'SoC_max' :
        eG5 = Val2
    else :
        eG5=0.95

    ### KNOWN INFO ### Faraday Constant
    if edt1 == 'Faraday_Constant' :
        eG6 = Val1
    elif edt2 == 'Faraday_Constant' :
        eG6 = Val2
    else :
        eG6=96585.3

        ### POSOLYTE ###

    ### KNOWN INFO ### Specific material costs, Posolyte Tank
    if edt1 == 'Posolyte_Tank' :
        eG14 = Val1
    elif edt2 == 'Posolyte_Tank' :
        eG14 = Val2
    else :
        eG14 = 1036

    ### KNOWN INFO ### Specific material costs, Active species posolyte
    if edt1 == 'Active_species_posolyte' :
        eG25 = Val1
    elif edt2 == 'Active_species_posolyte' :
        eG25 = Val2
    else :
        eG25=1380

    ### KNOWN INFO ### Specific material costs, Solvent posolyte
    if edt1 == 'Solvent_posolyte' :
        eG32 = Val1
    elif edt2 == 'Solvent_posolyte' :
        eG32 = Val2
    else :
        eG32=0.7

    ### KNOWN INFO ### Specific material costs, Additive posolyte
    if edt1 == 'Additive_posolyte' :
        eG38 = Val1
    elif edt2 == 'Additive_posolyte' :
        eG38 = Val2
    else :
        eG38=0

    ### KNOWN INFO ### Specific personnel costs, Fabrication posolyte
    if edt1 == 'Specific_personnel_costs_pos' :
        eG42 = Val1
    elif edt2 == 'Specific_personnel_costs_pos' :
        eG42 = Val2
    else :
        eG42=30

    ### KNOWN INFO ### Man hours, Fabrication posolyte
    if edt1 == 'Man_hours_pos' :
        eG43 = Val1
    elif edt2 == 'Man_hours_pos' :
        eG43 = Val2
    else :
        eG43=1/3


        ### NEGOLYTE ###

    ### KNOWN INFO ### Specific material costs, Negolyte Tank
    if edt1 == 'Negolyte_Tank' :
        eG46 = Val1
    elif edt2 == 'Negolyte_Tank' :
        eG46 = Val2
    else :
        eG46=1036

    ### KNOWN INFO ### Specific material costs, Active species negolyte
    if edt1 == 'Active_species_negolyte' :
        eG57 = Val1
    elif edt2 == 'Active_species_negolyte' :
        eG57 = Val2
    else :
        eG57=2805.28

    ### KNOWN INFO ### Specific material costs, Solvent negolyte
    if edt1 == 'Solvent_negolyte' :
        eG64 = Val1
    elif edt2 == 'Solvent_negolyte' :
        eG64 = Val2
    else :
        eG64=0.7

    ### KNOWN INFO ### Specific material costs, Additive negolyte
    if edt1 == 'Additive_negolyte' :
        eG70 = Val1
    elif edt2 == 'Additive_negolyte' :
        eG70 = Val2
    else :
        eG70=0

    ### KNOWN INFO ### Specific personnel costs, Fabrication negolyte
    if edt1 == 'Specific_personnel_costs_neg' :
        eG74 = Val1
    elif edt2 == 'Specific_personnel_costs_neg' :
        eG74 = Val2
    else :
        eG74=30

    ### KNOWN INFO ### Man hours, Fabrication negolyte
    if edt1 == 'Man_hours_neg' :
        eG75 = Val1
    elif edt2 == 'Man_hours_neg' :
        eG75 = Val2
    else :
        eG75=1/3


        # K SPACE ################################################################

        ### POSOLYTE ###

    ### KNOWN INFO ### Ohmic resistance, Posolyte
    if edt1 == 'Ohmic_resistance_pos' :
        eK17 = Val1
    elif edt2 == 'Ohmic_resistance_pos' :
        eK17 = Val2
    else :
        eK17=0.023

    ### KNOWN INFO ### E0posolyte, Posolyte
    if edt1 == 'E0posolyte' :
        eK20 = Val1
    elif edt2 == 'E0posolyte' :
        eK20 = Val2
    else :
        eK20=0.91

    ### KNOWN INFO ### Concentration, Active species posolyte
    if edt1 == 'Concentration_pos' :
        eK22 = Val1
    elif edt2 == 'Concentration_pos' :
        eK22 = Val2
    else :
        eK22=0.1

    ### KNOWN INFO ### Molecular weight, Active species posolyte
    if edt1 == 'Molecular_weight_pos' :
        eK23 = Val1
    elif edt2 == 'Molecular_weight_pos' :
        eK23 = Val2
    else :
        eK23=332.23

    ### KNOWN INFO ### z; equivalents per mol, Active species posolyte
    if edt1 == 'equivalents_per_mol_pos' :
        eK24 = Val1
    elif edt2 == 'equivalents_per_mol_pos' :
        eK24 = Val2
    else :
        eK24=2

    ### KNOWN INFO ### Concentration, Solvent posolyte
    if edt1 == 'Concentration_Sol_pos' :
        eK29 = Val1
    elif edt2 == 'Concentration_Sol_pos' :
        eK29 = Val2
    else :
        eK29=1

    ### KNOWN INFO ### Molecular weight, Solvent posolyte
    if edt1 == 'Molecular_weight_Sol_pos' :
        eK30 = Val1
    elif edt2 == 'Molecular_weight_Sol_pos' :
        eK30 = Val2
    else :
        eK30=98.079

    ### KNOWN INFO ### Concentration, CostsAddPos
    if edt1 == 'Concentration_CostsAddPos' :
        eK35 = Val1
    elif edt2 == 'Concentration_CostsAddPos' :
        eK35 = Val2
    else :
        eK35=0.05

    ### KNOWN INFO ### Molecular weight, Additive posolyte
    if edt1 == 'Molecular_weight_Add_pos' :
        eK36 = Val1
    elif edt2 == 'Molecular_weight_Add_pos' :
        eK36 = Val2
    else :
        eK36=97.994

        ### NEGOLYTE ###

    ### KNOWN INFO ### Ohmic resistance, Negolyte
    if edt1 == 'Ohmic_resistance_neg' :
        eK49 = Val1
    elif edt2 == 'Ohmic_resistance_neg' :
        eK49 = Val2
    else :
        eK49=0.023

    ### KNOWN INFO ### E0negolyte, Negolyte
    if edt1 == 'E0negolyte' :
        eK52 = Val1
    elif edt2 == 'E0negolyte' :
        eK52 = Val2
    else :
        eK52=0.21

    ### KNOWN INFO ### Concentration, Active species negolyte
    if edt1 == 'Concentration_neg' :
        eK54 = Val1
    elif edt2 == 'Concentration_neg' :
        eK54 = Val2
    else :
        #eK54=1.67
        eK54 = eK22

    ### KNOWN INFO ### Molecular weight, Active species negolyte
    if edt1 == 'Molecular_weight_neg' :
        eK55 = Val1
    elif edt2 == 'Molecular_weight_neg' :
        eK55 = Val2
    else :
        eK55=412.3

    ### KNOWN INFO ### Concentration, Solvent negolyte
    if edt1 == 'Concentration_Sol_neg' :
        eK61 = Val1
    elif edt2 == 'Concentration_Sol_neg' :
        eK61 = Val2
    else :
        eK61=1

    ### KNOWN INFO ### Molecular weight, Solvent negolyte
    if edt1 == 'Molecular_weight_Sol_neg' :
        eK62 = Val1
    elif edt2 == 'Molecular_weight_Sol_neg' :
        eK62 = Val2
    else :
        eK62=98.079

    ### KNOWN INFO ### Concentration, Additive negolyte
    if edt1 == 'Concentration_Add_neg' :
        eK67 = Val1
    elif edt2 == 'Concentration_Add_neg' :
        eK67 = Val2
    else :
        eK67=0.05

    ### KNOWN INFO ### Molecular weight, Additive negolyte
    if edt1 == 'Molecular_weight_Add_neg' :
        eK68 = Val1
    elif edt2 == 'Molecular_weight_Add_neg' :
        eK68 = Val2
    else :
        eK68=97.994

        ##############################################################################

        ###########################
        ######### POWER ###########
        ###########################

        # G SPACE #########################################################

    ### KNOWN INFO ### Required Power
    if edt1 == 'Required_Power' :
        pG2 = Val1
    elif edt2 == 'Required_Power' :
        pG2 = Val2
    else :
        pG2=0.547470138

        ### TEMPERATURE
        pG12=295

        ### GAS CONSTANT
        pG13=8.31447

        #-------------------------------------------------------------------

        ### INPUT OUTPUT ###

    ### KNOWN INFO ### Current Density, InputOutput
    if edt1 == 'Current_Density' :
        pG7 = Val1
    elif edt2 == 'Current_Density' :
        pG7 = Val2
    else :
        pG7=12.5

    ### KNOWN INFO ### AActive Area Cell, InputOutput
    if edt1 == 'AActive_Area_Cell' :
        pG8 = Val1
    elif edt2 == 'AActive_Area_Cell' :
        pG8 = Val2
    else :
        pG8=0.004

    #---------------------------------------------------------------------

    ### CURRENT COLLECTOR ###

    ### KNOWN INFO ### Specific material costs, Current collector
    if edt1 == 'Current_collector' :
        pG20 = Val1
    elif edt2 == 'Current_collector' :
        pG20 = Val2
    else :
        pG20=700

    ### KNOWN INFO ### Factor, Current collector
    if edt1 == 'Factor_Current_collector' :
        pG21 = Val1
    elif edt2 == 'Factor_Current_collector' :
        pG21 = Val2
    else :
        pG21=1.5

    ### KNOWN INFO ### Specific personnel costs, Current collector
    if edt1 == 'Specific_personnel_costs_Current_collector' :
        pG25 = Val1
    elif edt2 == 'Specific_personnel_costs_Current_collector' :
        pG25 = Val2
    else :
        pG25=30

    ### KNOWN INFO ### specific man hours, Current collector
    if edt1 == 'specific_man_hours_Current_collector' :
        pG26 = Val1
    elif edt2 == 'specific_man_hours_Current_collector' :
        pG26 = Val2
    else :
        pG26=1/12

    #----------------------------------------------------------------------

    ### ISOLATION PLATE ###

    ### KNOWN INFO ### Specific material costs, Isolation Plate
    if edt1 == 'Isolation_Plate' :
        pG28 = Val1
    elif edt2 == 'Isolation_Plate' :
        pG28 = Val2
    else :
        pG28=300

    ### KNOWN INFO ### Factor, Isolation Plate
    if edt1 == 'Factor_Isolation_Plate' :
        pG29 = Val1
    elif edt2 == 'Factor_Isolation_Plate' :
        pG29 = Val2
    else :
        pG29=2.3

    ### KNOWN INFO ### Specific fabrication costs, Isolation Plate
    if edt1 == 'Specific_fabrication_costs_Isolation_Plate' :
        pG33 = Val1
    elif edt2 == 'Specific_fabrication_costs_Isolation_Plate' :
        pG33 = Val2
    else :
        pG33=20

    #----------------------------------------------------------------------

    ### ENDPLATE ###

    ### KNOWN INFO ### Specific material costs, Endplate
    if edt1 == 'Endplate' :
        pG35 = Val1
    elif edt2 == 'Endplate' :
        pG35 = Val2
    else :
        pG35=200

    ### KNOWN INFO ### Specific Factor, Endplate
    if edt1 == 'Specific_Factor_endplate' :
        pG36 = Val1
    elif edt2 == 'Specific_Factor_endplate' :
        pG36 = Val2
    else :
        pG36=1.5

    ### KNOWN INFO ### Specific fabrication costs, Endplate
    if edt1 == 'Specific_fabrication_costs_Endplate' :
        pG40 = Val1
    elif edt2 == 'Specific_fabrication_costs_Endplate' :
        pG40 = Val2
    else :
        pG40=5

    #-----------------------------------------------------------------------

    ### CONNECTION ###

    ### KNOWN INFO ### Specific material costs, Connection
    if edt1 == 'Specific_material_costs_Connection' :
        pG42 = Val1
    elif edt2 == 'Specific_material_costs_Connection' :
        pG42 = Val2
    else :
        pG42=5

    #------------------------------------------------------------------------

    ### FINAL CELL & STACK ASSEMBLING

    ### KNOWN INFO ### Specific energy costs, Final Cell & Stack Assembling
    if edt1 == 'Specific_energy_costs' :
        pG47 = Val1
    elif edt2 == 'Specific_energy_costs' :
        pG47 = Val2
    else :
        pG47=0.3

    ### KNOWN INFO ### Energy, Final Cell & Stack Assembling
    if edt1 == 'Energy' :
        pG48 = Val1
    elif edt2 == 'Energy' :
        pG48 = Val2
    else :
        pG48=1

    ### KNOWN INFO ### Specific personnel costs, Final Cell & Stack Assembling
    if edt1 == 'Specific personnel costs' :
        pG49 = Val1
    elif edt2 == 'Specific personnel costs' :
        pG49 = Val2
    else :
        pG49=30

    ### KNOWN INFO ### Man hours, Final Cell & Stack Assembling
    if edt1 == 'Man_hours_Final_Cell' :
        pG51 = Val1
    elif edt2 == 'Man_hours_Final Cell' :
        pG51 = Val2
    else :
        pG51=2/3

    #-------------------------------------------------------------------------

    ### CELL ###

    ### KNOWN INFO ### Specific material costs, Membrane/Separator, Cell
    if edt1 == 'Specific_material_costs_Cell' :
        pG54 = Val1
    elif edt2 == 'Specific_material_costs_Cell' :
        pG54 = Val2
    else :
        pG54=2500

    ### KNOWN INFO ### Factor, Membrane/Separator, Cell
    if edt1 == 'Factor_Cell' :
        pG56 = Val1
    elif edt2 == 'Factor_Cell' :
        pG56 = Val2
    else :
        pG56=1.5

    ### KNOWN INFO ### Specific personnel costs, Membrane/Separator, Cell
    if edt1 == 'Specific_personnel_costs_Cell' :
        pG60 = Val1
    elif edt2 == 'Specific_personnel_costs_Cell' :
        pG60 = Val2
    else :
        pG60=30

    ### KNOWN INFO ### Man hours, Membrane/Separator, Cell
    if edt1 == 'Man_hours_Cell' :
        pG61 = Val1
    elif edt2 == 'Man_hours_Cell' :
        pG61 = Val2
    else :
        pG61=1/12

    ### KNOWN INFO ### Specific material costs, Felt Electrode, Cell
    if edt1 == 'Specific_material_costs_Felt_Electrode' :
        pG63 = Val1
    elif edt2 == 'Specific_material_costs_Felt_Electrode' :
        pG63 = Val2
    else :
        pG63=150

    ### KNOWN INFO ### Factor, Felt Electrode, Cell
    if edt1 == 'Factor_Felt_Electrode' :
        pG64 = Val1
    elif edt2 == 'Factor_Felt_Electrode' :
        pG64 = Val2
    else :
        pG64=1.5

    ### KNOWN INFO ### Specific fabrication costs, Felt Electrode, Cell
    if edt1 == 'Specific_fabrication_costs_Felt_Electrode' :
        pG69 = Val1
    elif edt2 == 'Specific_fabrication_costs_Felt_Electrode' :
        pG69 = Val2
    else :
        pG69=5

    ### KNOWN INFO ### Specific material costs, Bipolar plate, Cell
    if edt1 == 'Specific_material_costs_Bipolar_plate' :
        pG72 = Val1
    elif edt2 == 'Specific_material_costs_Bipolar_plate' :
        pG72 = Val2
    else :
        pG72=418

    ### KNOWN INFO ### Factor, Bipolar plate, Cell
    if edt1 == 'Factor_Bipolar_plate' :
        pG73 = Val1
    elif edt2 == 'Factor_Bipolar_plate' :
        pG73 = Val2
    else :
        pG73=1.3

    ### KNOWN INFO ### Specific fabrication costs, Bipolar plate, Cell
    if edt1 == 'Specific_fabrication_costs_Bipolar_plate' :
        pG77 = Val1
    elif edt2 == 'Specific_fabrication_costs_Bipolar_plate' :
        pG77 = Val2
    else :
    
        pG77=5

    ### KNOWN INFO ### Specific material costs, Gasket inside cell, Cell
    if edt1 == 'Specific_material_costs_Gasket' :
        pG79 = Val1
    elif edt2 == 'Specific_material_costs_Gasket' :
        pG79 = Val2
    else :
        pG79=1250

    ### KNOWN INFO ### Factor, Gasket inside cell, Cell
    if edt1 == 'Factor_Gasket' :
        pG80 = Val1
    elif edt2 == 'Factor_Gasket' :
        pG80 = Val2
    else :
        pG80=4

    ### KNOWN INFO ### Specific fabrication costs, Gasket inside cell, Cell
    if edt1 == 'Specific_fabrication_costs_Gasket' :
        pG84 = Val1
    elif edt2 == 'Specific_fabrication_costs_Gasket' :
        pG84 = Val2
    else :
        pG84=5

    ### KNOWN INFO ### Specific material costs, Cell frame Channel & Manifold , Cell
    if edt1 == 'Specific_material_costs_Cell_frame' :
        pG86 = Val1
    elif edt2 == 'Specific_material_costs_Cell_frame' :
        pG86 = Val2
    else :
        pG86=300

    ### KNOWN INFO ### Factor, Cell frame Channel & Manifold , Cell
    if edt1 == 'Factor_Cell_frame' :
        pG87 = Val1
    elif edt2 == 'Factor_Cell_frame' :
        pG87 = Val2
    else :
        pG87=1.5

    ### KNOWN INFO ### Specific personnel costs, Cell frame Channel & Manifold , Cell
    if edt1 == 'Specific_personnel_costs_Cell_frame' :
        pG89 = Val1
    elif edt2 == 'Specific_personnel_costs_Cell_fram' :
        pG89 = Val2
    else :
        pG89=30

    ### KNOWN INFO ### Man hours, Cell frame Channel & Manifold , Cell
    if edt1 == 'Man_hours_Cell_frame' :
        pG90 = Val1
    elif edt2 == 'Man_hours_Cell_frame' :
        pG90 = Val2
    else :
        pG90=20

    ### KNOWN INFO ### Cost Screws, Screws, Cell
    if edt1 == 'Cost_Screws' :
        pG93 = Val1
    elif edt2 == 'Cost_Screws' :
        pG93 = Val2
    else :
        pG93=16.58

    ### KNOWN INFO ### Specific material costs, Carbon Paper, Cell
    if edt1 == 'Specific_material_costs_Carbon_Paper' :
        pG95 = Val1
    elif edt2 == 'Specific_material_costs_Carbon_Paper' :
        pG95 = Val2
    else :
        pG95=1500

    ### KNOWN INFO ### Factor, Carbon Paper, Cell
    if edt1 == 'Factor_Carbon_Paper' :
        pG96 = Val1
    elif edt2 == 'Factor_Carbon_Paper' :
        pG96 = Val2
    else :
        pG96=5

    ### KNOWN INFO ### Specific fabrication costs, Carbon Paper, Cell
    if edt1 == 'Specific_fabrication_costs_Carbon_Paper' :
        pG100 = Val1
    elif edt2 == 'Specific_fabrication_costs_Carbon_Paper' :
        pG100 = Val2
    else :
        pG100=5

        #---------------------------------------------------------------------------------

        ### FITTINGS ###

    ### KNOWN INFO ### CostsFittings, Fittings
    if edt1 == 'CostsFittings' :
        pG101 = Val1
    elif edt2 == 'CostsFittings' :
        pG101 = Val2
    else :
        pG101=146.66

    #####################################################################

    ### KNOWN INFO ### NStacks, InputOutput
    if edt1 == 'NStacks' :
        pH11 = Val1
    elif edt2 == 'NStacks' :
        pH11 = Val2
    else :
        pH11=1

    #####################################################################

    ### KNOWN INFO ### Specific ohmic resistance, Current collector
    if edt1 == 'Specific_ohmic_resistance' :
        pK20 = Val1
    elif edt2 == 'Specific_ohmic_resistance' :
        pK20 = Val2
    else :
        pK20=0.017241

    ### KNOWN INFO ### Length, Current collector
    if edt1 == 'Length' :
        pK23 = Val1
    elif edt2 == 'Length' :
        pK23 = Val2
    else :
        pK23=0.15

    ### KNOWN INFO ### Specific ohmic resistance, Membrane Separator, Cell
    if edt1 == 'Specific_ohmic_resistance_Membrane' :
        pK54 = Val1
    elif edt2 == 'Specific_ohmic_resistance_Membrane' :
        pK54 = Val2
    else :
        pK54=0.65

    ### KNOWN INFO ### Width, Membrane Separator, Cell
    if edt1 == 'Width' :
        pK57 = Val1
    elif edt2 == 'Width' :
        pK57 = Val2
    else :
        pK57=0.00005

    ### KNOWN INFO ### Specific ohmic resistance, Felt Electrode, Cell
    if edt1 == 'Specific_ohmic_resistance_Electrode' :
        pK63 = Val1
    elif edt2 == 'Specific_ohmic_resistance_Electrode' :
        pK63 = Val2
    else :
        pK63=0.00322

    ### KNOWN INFO ### Thickness, Felt Electrode, Cell
    if edt1 == 'Thickness' :
        pK66 = Val1
    elif edt2 == 'Thickness' :
        pK66 = Val2
    else :
        pK66=0.00465

    ### KNOWN INFO ### Specific ohmic resistance, Bipolar plate, Cell
    if edt1 == 'Specific_ohmic_resistance_Bipolar' :
        pK75 = Val1
    elif edt2 == 'Specific_ohmic_resistance_Bipolar' :
        pK75 = Val2
    else :
        pK75=0.000045

    ### KNOWN INFO ### Thickness, Bipolar plate, Cell
    if edt1 == 'Thickness_Bipolar' :
        pK74 = Val1
    elif edt2 == 'Thickness_Bipolar' :
        pK74 = Val2
    else :
        pK74=0.003

    ### KNOWN INFO ### Specific ohmic resistance, Carbon Paper, Cell
    if edt1 == 'Specific_ohmic_resistance_Carbon_Paper' :
        pK95 = Val1
    elif edt2 == 'Specific_ohmic_resistance_Carbon_Paper' :
        pK95 = Val2
    else :
        pK95=0.006

    ### KNOWN INFO ### Thickness, Carbon Paper, Cell
    if edt1 == 'Thickness_Carbon_Paper' :
        pK96 = Val1
    elif edt2 == 'Thickness_Carbon_Paper' :
        pK96 = Val2
    else :
        pK96=0.00009

        ##############################
        ### VOLTAGE AND RESISTANCE ###
        ##############################

    ### KNOWN INFO ### Activation overpotential
    if edt1 == 'Activation_overpotential' :
        vrG4 = Val1
    elif edt2 == 'Activation_overpotential' :
        vrG4 = Val2
    else :
        vrG4 = 0.05

    ### KNOWN INFO ### Concentration overpotential
    if edt1 == 'Concentration_overpotential' :
        vrG5 = Val1
    elif edt2 == 'Concentration_overpotential' :
        vrG5 = Val2
    else :
        vrG5 = 0.2

    

    ######################################
    ###### END OF GREEN VALUES ###########
    ######################################


    ##############################
    #### POWER INITIAL SPACE #####
    ##############################

    if edt1 == 'Current' :
        pH6 = Val1
    elif edt2 == 'Current' :
        pH6 = Val2
    else :
        pH6=pG7*pG8*(10**4)*(10**-3)

    if edt1 == 'Ustack' :
        pH4 = Val1
    elif edt2 == 'Ustack' :
        pH4 = Val2
    else :
        pH4=round(pG2/pH6,3)

    ##############################
    ####### POWER K SPACE ########
    ##############################

    if edt1 == 'Specific_ohmic_resistance_Current_Collector' :
        pK21 = Val1
    elif edt2 == 'Specific_ohmic_resistance_Current_Collector' :
        pK21 = Val2
    else :
        pK21=(pK20/pK23)*(10**-6)

    if edt1 == 'Resistance_Current_Collector' :
        pK19 = Val1
    elif edt2 == 'Resistance_Current_Collector' :
        pK19 = Val2
    else :
        pK19=pK21*pK23/pG8

    if edt1 == 'Specific_ohmic_resistance_Membrane' :
        pK55 = Val1
    elif edt2 == 'Specific_ohmic_resistance_Membrane' :
        pK55 = Val2
    else :
        pK55=(pK54*(10**-4)/pK57)

    if edt1 == 'Resistance_Membrane' :
        pK53 = Val1
    elif edt2 == 'Resistance_Membrane' :
        pK53 = Val2
    else :
        pK53=pK55*pK57/pG8

    if edt1 == 'Resistance_Felt' :
        pK62 = Val1
    elif edt2 == 'Resistance_Felt' :
        pK62 = Val2
    else :
        pK62=pK63*pK66/pG8

    if edt1 == 'Conductivity_BPP' :
        pK73 = Val1
    elif edt2 == 'Conductivity_BPP' :
        pK73 = Val2
    else :
        pK73=1/pK75

    if edt1 == 'Resistance_BPP' :
        pK71 = Val1
    elif edt2 == 'Resistance_BPP' :
        pK71 = Val2
    else :
        pK71=1/pK73*pK74/pG8

    if edt1 == 'Resistance_Carbon_Paper' :
        pK94 = Val1
    elif edt2 == 'Resistance_Carbon_Paper' :
        pK94 = Val2
    else :
        pK94=pK95*pK96/pG8

    ##############################
    #### ENERGY INITIAL SPACE ####
    ##############################

    if edt1 == 'Required_Energy' :
        eG2 = Val1
    elif edt2 == 'Required_Energy' :
        eG2 = Val2
    else :
        eG2=pG2*10

    if edt1 == 'Charge_density' :
        eG7 = Val1
    elif edt2 == 'Charge_density' :
        eG7 = Val2
    else :
        eG7=eK24*eG6*eK22/3600

    ##############################
    ### VOLTAGE AND RESISTANCE ###
    ##############################

    if edt1 == 'R_current_collector' :
        vrG7 = Val1
    elif edt2 == 'R_current_collector' :
        vrG7 = Val2
    else :
        vrG7=pK19

    if edt1 == 'R_membrane' :
        vrG8 = Val1
    elif edt2 == 'R_membrane' :
        vrG8 = Val2
    else :
        vrG8=pK53

    if edt1 == 'R_electrode' :
        vrG9 = Val1
    elif edt2 == 'R_electrode' :
        vrG9 = Val2
    else :
        vrG9=2*pK62

    if edt1 == 'R_bipolar_plate' :
        vrG10 = Val1
    elif edt2 == 'R_bipolar_plate' :
        vrG10 = Val2
    else :
        vrG10=pK71

    if edt1 == 'R_posolyte' :
        vrG11 = Val1
    elif edt2 == 'R_posolyte' :
        vrG11 = Val2
    else :
        vrG11=eK17

    if edt1 == 'R_negolyte' :
        vrG12 = Val1
    elif edt2 == 'R_negolyte' :
        vrG12 = Val2
    else :
        vrG12=eK49

    if edt1 == 'R_carbon_paper' :
        vrG13 = Val1
    elif edt2 == 'R_carbon_paper' :
        vrG13 = Val2
    else :
        vrG13=2*pK94

    if edt1 == 'U_OCV' :
        vrG3 = Val1
    elif edt2 == 'U_OCV' :
        vrG3 = Val2
    else :
        vrG3= eK20 - eK52 + ((pG13*pG12)/(eK24*eG6))*2*log(eG5/eG4)

    if edt1 == 'I_stack' :
        vrG15 = Val1
    elif edt2 == 'I_stack' :
        vrG15 = Val2
    else :
        vrG15 = pH6

    if edt1 == 'R_inner' :
        vrH14 = Val1
    elif edt2 == 'R_inner' :
        vrH14 = Val2
    else :
        vrH14= vrG7 + vrG8 + vrG9 + vrG10 + vrG11 + vrG12 + vrG13

    if edt1 == 'U_ohm' :
        vrG6 = Val1
    elif edt2 == 'U_ohm' :
        vrG6 = Val2
    else :
        vrG6 = vrG15*vrH14

    ################################
    ######## U_cell and party ######
    ################################

    if edt1 == 'U_cell' :
        pH5 = Val1
    elif edt2 == 'U_cell' :
        pH5 = Val2
    else :
        pH5 = vrG3-vrG4-vrG5-vrG6

    global pH10
    if edt1 == 'Ncells' :
        pH10 = Val1
    elif edt2 == 'Ncells' :
        pH10 = Val2
    else :
        pH10 = math.ceil(pH4/pH5)

    if edt1 == 'Active_Area' :
        pH9 = Val1
    elif edt2 == 'Active_Area' :
        pH9 = Val2
    else :
        pH9=pG8*pH10

    ###########################
    ######### POWER ###########
    ###########################

    if edt1 == 'Factor_Current_Collector' :
        pG22 = Val1
    elif edt2 == 'Factor_Current_Collector' :
        pG22 = Val2
    else :
        pG22=2*pH11

    if edt1 == 'Cost_Material_Current_Collector' :
        pG23 = Val1
    elif edt2 == 'Cost_Material_Current_Collector' :
        pG23 = Val2
    else :
        pG23=pG22*pG21*pH9*pG20

    if edt1 == 'Fabrication_Cost_Current_Collector' :
        pG24 = Val1
    elif edt2 == 'Fabrication_Cost_Current_Collector' :
        pG24 = Val2
    else :
        pG24=pG25*pG26*pG22

    if edt1 == 'Cost_Current_Collector' :
        pG19 = Val1
    elif edt2 == 'Cost_Current_Collector' :
        pG19 = Val2
    else :
        pG19=pG23+pG24

    if edt1 == 'Factor_Isolation_Plate' :
        pG30 = Val1
    elif edt2 == 'Factor_Isolation_Plate' :
        pG30 = Val2
    else :
        pG30=pH11

    if edt1 == 'Cost_Material_Isolation_Plate' :
        pG31 = Val1
    elif edt2 == 'Cost_Material_Isolation_Plate' :
        pG31 = Val2
    else :
        pG31=pG30*pG29*pH9*pG28

    if edt1 == 'Fabrication_Costs_Isolation_Plate' :
        pG32 = Val1
    elif edt2 == 'Fabrication_Costs_Isolation_Plate' :
        pG32 = Val2
    else :
        pG32=pG33*pG30

    if edt1 == 'Costs_Isolation_Plate' :
        pG27 = Val1
    elif edt2 == 'Costs_Isolation_Plate' :
        pG27 = Val2
    else :
        pG27=pG31+pG32

    if edt1 == 'Factor_Endplate' :
        pG37 = Val1
    elif edt2 == 'Factor_Endplate' :
        pG37 = Val2
    else :
        pG37=2*pH11

    if edt1 == 'Material_costs_Endplate' :
        pG38 = Val1
    elif edt2 == 'Material_costs_Endplate' :
        pG38 = Val2
    else :
        pG38=pG37*pG36*pH9*pG35

    if edt1 == 'Fabrication_costs_Endplate' :
        pG39 = Val1
    elif edt2 == 'Fabrication_costs_Endplate' :
        pG39 = Val2
    else :
        pG39=pG40*pG37

    if edt1 == 'Costs_Endplate' :
        pG34 = Val1
    elif edt2 == 'Costs_Endplate' :
        pG34 = Val2
    else :
        pG34=pG38+pG39

    if edt1 == 'Factor_Connection' :
        pG43 = Val1
    elif edt2 == 'Factor_Connection' :
        pG43 = Val2
    else :
        pG43=4*pH11

    if edt1 == 'Material_costs_Connection' :
        pG44 = Val1
    elif edt2 == 'Material_costs_Connection' :
        pG44 = Val2
    else :
        pG44=pG42*pG43

    if edt1 == 'Costs_Connection' :
        pG41 = Val1
    elif edt2 == 'Costs_Connection' :
        pG41 = Val2
    else :
        pG41=pG44

    if edt1 == 'Factor_Stack&Assembly' :
        pG46 = Val1
    elif edt2 == 'Factor_Stack&Assembly' :
        pG46 = Val2
    else :
        pG46=pH10+pH11

    if edt1 == 'CostsFCSA' :
        pG45 = Val1
    elif edt2 == 'CostsFCSA' :
        pG45 = Val2
    else :
        pG45=((pG47*pG48)+(pG49*pG51))*pG46

    if edt1 == 'Factor_Membrane' :
        pG57 = Val1
    elif edt2 == 'Factor_Membrane' :
        pG57 = Val2
    else :
        pG57=1*pH10

    if edt1 == 'Material costs_Membrane' :
        pG58 = Val1
    elif edt2 == 'Material costs_Membrane' :
        pG58 = Val2
    else :
        pG58=pG57*pG56*pG8*pG54

    if edt1 == 'Fabrication_costs_Membrane' :
        pG59 = Val1
    elif edt2 == 'Fabrication_costs_Membrane' :
        pG59 = Val2
    else :
        pG59=pG60*pG61*pG57

    if edt1 == 'Costs_Membrane' :
        pG53 = Val1
    elif edt2 == 'Costs_Membrane' :
        pG53 = Val2
    else :
        pG53=pG58+pG59

    if edt1 == 'Factor_Felt' :
        pG66 = Val1
    elif edt2 == 'Factor_Felt' :
        pG66 = Val2
    else :
        pG66=2*pH10

    if edt1 == 'Material_costs_Felt' :
        pG67 = Val1
    elif edt2 == 'Material_costs_Felt' :
        pG67 = Val2
    else :
        pG67=pG66*pG64*pG8*pG63

    if edt1 == 'Fabrication_costs_Felt' :
        pG68 = Val1
    elif edt2 == 'Fabrication_costs_Felt' :
        pG68 = Val2
    else :
        pG68=pG69*pG66

    if edt1 == 'Costs_Felt' :
        pG62 = Val1
    elif edt2 == 'Costs_Felt' :
        pG62 = Val2
    else :
        pG62=pG67+pG68

    if edt1 == 'Factor_BPP' :
        pG74 = Val1
    elif edt2 == 'Factor_BPP' :
        pG74 = Val2
    else :
        pG74=pH10+1

    if edt1 == 'Material_costs_BPP' :
        pG75 = Val1
    elif edt2 == 'Material_costs_BPP' :
        pG75 = Val2
    else :
        pG75=pG74*pG73*pG8*pG72

    if edt1 == 'Fabrication_costs_BPP' :
        pG76 = Val1
    elif edt2 == 'Fabrication_costs_BPP' :
        pG76 = Val2
    else :
        pG76=pG77*pG74

    if edt1 == 'Costs_BPP' :
        pG71 = Val1
    elif edt2 == 'Costs_BPP' :
        pG71 = Val2
    else :
        pG71=pG75+pG76

    if edt1 == 'Factor_Gasket' :
        pG81 = Val1
    elif edt2 == 'Factor_Gasket' :
        pG81 = Val2
    else :
        pG81=6*pH10

    if edt1 == 'Material_costs_Gasket' :
        pG82 = Val1
    elif edt2 == 'Material_costs_Gasket' :
        pG82 = Val2
    else :
        pG82=pG81*pG80*pG8*pG79

    if edt1 == 'Fabrication_costs_Gasket' :
        pG83 = Val1
    elif edt2 == 'Fabrication_costs_Gasket' :
        pG83 = Val2
    else :
        pG83=pG84*pG81

    if edt1 == 'CostsGasket' :
        pG78 = Val1
    elif edt2 == 'CostsGasket' :
        pG78 = Val2
    else :
        pG78=pG82+pG83

    if edt1 == 'Factor_Cellframe' :
        pG88 = Val1
    elif edt2 == 'Factor_Cellframe' :
        pG88 = Val2
    else :
        pG88=2*pH10

    if edt1 == 'Material_costs_Cellframe' :
        pG91 = Val1
    elif edt2 == 'Material_costs_Cellframe' :
        pG91 = Val2
    else :
        pG91=pG86*pG8*pG87*pG88

    if edt1 == 'Fabrication_costs_Cellframe' :
        pG92 = Val1
    elif edt2 == 'Fabrication_costs_Cellframe' :
        pG92 = Val2
    else :
        pG92=pG90*pG89

    if edt1 == 'CostsCellframe' :
        pG85 = Val1
    elif edt2 == 'CostsCellframe' :
        pG85 = Val2
    else :
        pG85=pG91+pG92

    if edt1 == 'Screws' :
        pG93 = Val1
    elif edt2 == 'Screws' :
        pG93 = Val2
    else :
        pG93=16.58*pH11

    if edt1 == 'Factor_Carbon_Paper' :
        pG97 = Val1
    elif edt2 == 'Factor_Carbon_Paper' :
        pG97 = Val2
    else :
        pG97=2*pH10

    if edt1 == 'Material_costs_Carbon_Paper' :
        pG98 = Val1
    elif edt2 == 'Material_costs_Carbon_Paper' :
        pG98 = Val2
    else :
        pG98=pG95*pG8*pG96*pG97

    if edt1 == 'Fabrication_costs_Carbon_Paper' :
        pG99 = Val1
    elif edt2 == 'Fabrication_costs_Carbon_Paper' :
        pG99 = Val2
    else :
        pG99=pG100*pG97

    if edt1 == 'CostsCarbon_Paper' :
        pG94 = Val1
    elif edt2 == 'CostsCarbon_Paper' :
        pG94 = Val2
    else :
        pG94=pG98+pG99

    if edt1 == 'CostsCell' :
        pG52 = Val1
    elif edt2 == 'CostsCell' :
        pG52 = Val2
    else :
        pG52=pG53+pG62+pG71+pG78+pG85+pG93+pG94+pG101

    # CostsPower
    if edt1 == 'Cost_Power' :
        pG18 = Val1
    elif edt2 == 'Cost_Power' :
        pG18 = Val2
    else :
        pG18=pG19+pG27+pG34+pG41+pG45+pG52

    ###########################
    ######### ENERGY ##########
    ###########################

    if edt1 == 'Volume_Pos_Tank' :
        eG13 = Val1
    elif edt2 == 'Volume_Pos_Tank' :
        eG13 = Val2
    else :
        eG13=eG2/(pH5*(eG5-eG4)*eG7)

    global eG16
    if edt1 == 'Volume_Pos' :
        eG16 = Val1
    elif edt2 == 'Volume_Pos' :
        eG16 = Val2
    else :
        eG16=eG13

    global eG12
    if edt1 == 'CostsPosTank' :
        eG12 = Val1
    elif edt2 == 'CostsPosTank' :
        eG12 = Val2
    else :
        eG12=eG13*eG14

    if edt1 == 'Volume_Act_Spec_Pos' :
        eG23 = Val1
    elif edt2 == 'Volume_Act_Spec_Pos' :
        eG23 = Val2
    else :
        eG23=eG16

    global eG22
    if edt1 == 'CostsActSpecPos' :
        eG22 = Val1
    elif edt2 == 'CostsActSpecPos' :
        eG22 = Val2
    else :
        eG22=eK23*eK22*eG23*eG25/1000

    if edt1 == 'Volume_Sol_Pos' :
        eG30 = Val1
    elif edt2 == 'Volume_Sol_Pos' :
        eG30 = Val2
    else :
        eG30=eG16

    global eG29
    if edt1 == 'CostsSolvPos' :
        eG29 = Val1
    elif edt2 == 'CostsSolvPos' :
        eG29 = Val2
    else :
        eG29=eK30*eK29*eG30*eG32/1000

    if edt1 == 'Volume_Add_Pos' :
        eG36 = Val1
    elif edt2 == 'Volume_Add_Pos' :
        eG36 = Val2
    else :
        eG36=eG16

    if edt1 == 'Specific_material_costs' :
        eG40 = Val1
    elif edt2 == 'Specific_material_costs' :
        eG40 = Val2
    else :
        eG40=eG38*eK36/1000

    global eG35
    if edt1 == 'CostsAddPos' :
        eG35 = Val1
    elif edt2 == 'CostsAddPos' :
        eG35 = Val2
    else :
        eG35=eK35*eG40*eG36

    global eG41
    if edt1 == 'CostsFabPos' :
        eG41 = Val1
    elif edt2 == 'CostsFabPos' :
        eG41 = Val2
    else :
        eG41=eG42*eG43

    if edt1 == 'CostsPosolyte' :
        eG15 = Val1
    elif edt2 == 'CostsPosolyte' :
        eG15 = Val2
    else :
        eG15=eG22+eG29+eG35+eG41

    if edt1 == 'Volume_Neg_Tank' :
        eG45 = Val1
    elif edt2 == 'Volume_Neg_Tank' :
        eG45 = Val2
    else :
        eG45=eG16

    global eG44
    if edt1 == 'CostsNegTank' :
        eG44 = Val1
    elif edt2 == 'CostsNegTank' :
        eG44 = Val2
    else :
        eG44=eG45*eG46

    if edt1 == 'Volume_Act_Spec_Neg' :
        eG55 = Val1
    elif edt2 == 'Volume_Act_Spec_Neg' :
        eG55 = Val2
    else :
        eG55=eG16

    global eG54
    if edt1 == 'CostsActSpecNeg' :
        eG54 = Val1
    elif edt2 == 'CostsActSpecNeg' :
        eG54 = Val2
    else :
        eG54=eK55*eK54*eG55*eG57/1000

    if edt1 == 'Volume_Sol_Neg' :
        eG62 = Val1
    elif edt2 == 'Volume_Sol_Neg' :
        eG62 = Val2
    else :
        eG62=eG16

    global eG61
    if edt1 == 'CostsSolvNeg' :
        eG61 = Val1
    elif edt2 == 'CostsSolvNeg' :
        eG61 = Val2
    else :
        eG61=eK62*eK61*eG62*eG64/1000

    if edt1 == 'Volume_Act_Neg' :
        eG68 = Val1
    elif edt2 == 'Volume_Act_Neg' :
        eG68 = Val2
    else :
        eG68=eG16

    if edt1 == 'Specific_material_costs' :
        eG72 = Val1
    elif edt2 == 'Specific_material_costs' :
        eG72 = Val2
    else :
        eG72=eG70*eK68/1000

    global eG67
    if edt1 == 'CostsAddNeg' :
        eG67 = Val1
    elif edt2 == 'CostsAddNeg' :
        eG67 = Val2
    else :
        eG67=eK67*eG72*eG68

    global eG73
    if edt1 == 'CostsFabNeg' :
        eG73 = Val1
    elif edt2 == 'CostsFabNeg' :
        eG73 = Val2
    else :
        eG73=eG74*eG75

    #CostsNegolyte
    if edt1 == 'CostsNegolyte' :
        eG47 = Val1
    elif edt2 == 'CostsNegolyte' :
        eG47 = Val2
    else :
        eG47=eG54+eG61+eG67+eG73

    #CostsEnergy
    if edt1 == 'CostsPosolyte' :
        eG11 = Val1
    elif edt2 == 'CostsPosolyte' :
        eG11 = Val2
    else :
        eG11=eG12+eG15+eG44+eG47

    ##############################
    ######### VARIATION ##########
    ##############################

    global vB4
    #Costs_Power
    if edt1 == '"CostsPower_Var' :
        vB4 = Val1
    elif edt2 == 'CostsPower_Var' :
        vB4 = Val2
    else :
        vB4 = pG18
        
    global vF4
    #Costs_Energy
    if edt1 == 'CostsEnergy_Var' :
        vF4 = Val1
    elif edt2 == 'CostsEnergy_Var' :
        vF4 = Val2
    else :
        vF4 = eG11
        
    #Energy_Capacity
    if edt1 == 'Energy_Capacity' :
        vH4 = Val1
    elif edt2 == 'Energy_Capacity' :
        vH4 = Val2
    else :
        vH4 = eG2
        
    #Costs_Battery
    if edt1 == 'Costs_Battery' :
        vJ4 = Val1
    elif edt2 == 'Costs_Battery' :
        vJ4 = Val2
    else :
        vJ4 = (vB4+vF4)/vH4
        
    return vJ4

SVF('Current_Density', 'Concentration_pos', 12.5, 0.1)
print(vB4)
print(pH10)
print(vF4)
print(eG16*2)