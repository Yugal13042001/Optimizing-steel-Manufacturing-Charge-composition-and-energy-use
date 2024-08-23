import pandas as pd
data = pd.read_csv(r"C:\Users\Admin\Desktop\C0DE\steeel.csv")
print(data)

data.columns=data.columns.str.strip()

#------------------------------------------------------------------------------------------------------------------
#Handling Duplicates

data.drop_duplicates(inplace = True)
print(data)



#outlier detection
#BOXPLOT
#---------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r"C:\Users\Admin\Desktop\C0DE\steeel.csv")
print(data)

data.columns=data.columns.str.strip()
# INJ1_QTY
plt.figure(figsize=(8, 6))
plt.boxplot(data['INJ1_QTY'], vert=False, sym='b.')
plt.title('Box plot of INJ1_QTY to find outliers')
plt.xlabel('Values')
plt.tight_layout()
plt.show()

# Boxplot for INJ2_QTY
plt.figure(figsize=(8, 6))
plt.boxplot(data['INJ2_QTY'], vert=False, sym='b.')
plt.title('Boxplot of INJ2_QTY')
plt.xlabel('INJ2_QTY values')
plt.tight_layout()
plt.show()

# Boxplot for TP
plt.figure(figsize=(8, 6))
plt.boxplot(data['TP'], vert=False, sym='b.')
plt.title('Boxplot of TP')
plt.xlabel('TP values')
plt.tight_layout()
plt.show()

# Boxplot for BSM
plt.figure(figsize=(8, 6))
plt.boxplot(data['BSM'], vert=False, sym='b.')
plt.title('Boxplot of BSM')
plt.xlabel('BSM values')
plt.tight_layout()
plt.show()

# Boxplot for MSTB
plt.figure(figsize=(8, 6))
plt.boxplot(data['MSTB'], vert=False, sym='b.')
plt.title('Boxplot of MSTB')
plt.xlabel('MSTB values')
plt.tight_layout()
plt.show()

# Boxplot for SKULL
plt.figure(figsize=(8, 6))
plt.boxplot(data['SKULL'], vert=False, sym='b.')
plt.title('Boxplot of SKULL')
plt.xlabel('SKULL values')
plt.tight_layout()
plt.show()

# Boxplot for SHRAD
plt.figure(figsize=(8, 6))
plt.boxplot(data['SHRAD'], vert=False, sym='b.')
plt.title('Boxplot of SHRAD')
plt.xlabel('SHRAD values')
plt.tight_layout()
plt.show()



# Boxplot for REMET
plt.figure(figsize=(8, 6))
plt.boxplot(data['REMET'], vert=False, sym='b.')
plt.title('Boxplot of REMET')
plt.xlabel('REMET values')
plt.tight_layout()
plt.show()

# Boxplot for BP
plt.figure(figsize=(8, 6))
plt.boxplot(data['BP'], vert=False, sym='b.')
plt.title('Boxplot of BP')
plt.xlabel('BP values')
plt.tight_layout()
plt.show()

# Boxplot for HBI
plt.figure(figsize=(8, 6))
plt.boxplot(data['HBI'], vert=False, sym='b.')
plt.title('Boxplot of HBI')
plt.xlabel('HBI values')
plt.tight_layout()
plt.show()

# Boxplot for OTHERS
plt.figure(figsize=(8, 6))
plt.boxplot(data['OTHERS'], vert=False, sym='b.')
plt.title('Boxplot of OTHERS')
plt.xlabel('OTHERS values')
plt.tight_layout()
plt.show()

# Boxplot for SCRAP_QTY
plt.figure(figsize=(8, 6))
plt.boxplot(data['SCRAP_QTY'], vert=False, sym='b.')
plt.title('Boxplot of SCRAP_QTY')
plt.xlabel('SCRAP_QTY values')
plt.tight_layout()
plt.show()

# Boxplot for PIGIRON
plt.figure(figsize=(8, 6))
plt.boxplot(data['PIGIRON'], vert=False, sym='b.')
plt.title('Boxplot of PIGIRON')
plt.xlabel('PIGIRON values')
plt.tight_layout()
plt.show()

# Boxplot for DRI1_QTY
plt.figure(figsize=(8, 6))
plt.boxplot(data['DRI1_QTY'], vert=False, sym='b.')
plt.title('Boxplot of DRI1_QTY')
plt.xlabel('DRI1_QTY values')
plt.tight_layout()
plt.show()

# Boxplot for DRI2_QTY
plt.figure(figsize=(8, 6))
plt.boxplot(data['DRI2_QTY'], vert=False, sym='b.')
plt.title('Boxplot of DRI2_QTY')
plt.xlabel('DRI2_QTY values')
plt.tight_layout()
plt.show()

# Boxplot for TOT_DRI_QTY
plt.figure(figsize=(8, 6))
plt.boxplot(data['TOT_DRI_QTY'], vert=False, sym='b.')
plt.title('Boxplot of TOT_DRI_QTY')
plt.xlabel('TOT_DRI_QTY values')
plt.tight_layout()
plt.show()

# Boxplot for HOT_METAL
plt.figure(figsize=(8, 6))
plt.boxplot(data['HOT_METAL'], vert=False, sym='b.')
plt.title('Boxplot of HOT_METAL')
plt.xlabel('HOT_METAL values')
plt.tight_layout()
plt.show()

# Boxplot for TotalCharge
plt.figure(figsize=(8, 6))
plt.boxplot(data['TotalCharge'], vert=False, sym='b.')
plt.title('Boxplot of TotalCharge')
plt.xlabel('TotalCharge values')
plt.tight_layout()
plt.show()

# Boxplot for Hot_Heel
plt.figure(figsize=(8, 6))
plt.boxplot(data['Hot_Heel'], vert=False, sym='b.')
plt.title('Boxplot of Hot_Heel')
plt.xlabel('Hot_Heel values')
plt.tight_layout()
plt.show()

# Boxplot for DOLO
plt.figure(figsize=(8, 6))
plt.boxplot(data['DOLO'], vert=False, sym='b.')
plt.title('Boxplot of DOLO')
plt.xlabel('DOLO values')
plt.tight_layout()
plt.show()

# Boxplot for DOLO1_EMPTY
plt.figure(figsize=(8, 6))
plt.boxplot(data['DOLO1_EMPTY'], vert=False, sym='b.')
plt.title('Boxplot of DOLO1_EMPTY')
plt.xlabel('DOLO1_EMPTY values')
plt.tight_layout()
plt.show()

# Boxplot for TOT_LIME_QTY
plt.figure(figsize=(8, 6))
plt.boxplot(data['TOT_LIME_QTY'], vert=False, sym='b.')
plt.title('Boxplot of TOT_LIME_QTY')
plt.xlabel('TOT_LIME_QTY values')
plt.tight_layout()
plt.show()

# Boxplot for TAP_TEMP
plt.figure(figsize=(8, 6))
plt.boxplot(data['TAP_TEMP'], vert=False, sym='b.')
plt.title('Boxplot of TAP_TEMP')
plt.xlabel('TAP_TEMP values')
plt.tight_layout()
plt.show()

# Boxplot for O2REQ
plt.figure(figsize=(8, 6))
plt.boxplot(data['O2REQ'], vert=False, sym='b.')
plt.title('Boxplot of O2REQ')
plt.xlabel('O2REQ values')
plt.tight_layout()
plt.show()

# Boxplot for O2ACT
plt.figure(figsize=(8, 6))
plt.boxplot(data['O2ACT'], vert=False, sym='b.')
plt.title('Boxplot of O2ACT')
plt.xlabel('O2ACT values')
plt.tight_layout()
plt.show()

# Boxplot for ENERGY
plt.figure(figsize=(8, 6))
plt.boxplot(data['ENERGY'], vert=False, sym='b.')
plt.title('Boxplot of ENERGY')
plt.xlabel('ENERGY values')
plt.tight_layout()
plt.show()

# Boxplot for KWH_PER_TON
plt.figure(figsize=(8, 6))
plt.boxplot(data['KWH_PER_TON'], vert=False, sym='b.')
plt.title('Boxplot of KWH_PER_TON')
plt.xlabel('KWH_PER_TON values')
plt.tight_layout()
plt.show()

# Boxplot for KWH_PER_MIN
plt.figure(figsize=(8, 6))
plt.boxplot(data['KWH_PER_MIN'], vert=False, sym='b.')
plt.title('Boxplot of KWH_PER_MIN')
plt.xlabel('KWH_PER_MIN values')
plt.tight_layout()
plt.show()

# Boxplot for MELT_TIME
plt.figure(figsize=(8, 6))
plt.boxplot(data['MELT_TIME'], vert=False, sym='b.')
plt.title('Boxplot of MELT_TIME')
plt.xlabel('MELT_TIME values')
plt.tight_layout()
plt.show()

# Boxplot for TA_TIME
plt.figure(figsize=(8, 6))
plt.boxplot(data['TA_TIME'], vert=False, sym='b.')
plt.title('Boxplot of TA_TIME')
plt.xlabel('TA_TIME values')
plt.tight_layout()
plt.show()

# Boxplot for TT_TIME
plt.figure(figsize=(8, 6))
plt.boxplot(data['TT_TIME'], vert=False, sym='b.')
plt.title('Boxplot of TT_TIME')
plt.xlabel('TT_TIME values')
plt.tight_layout()
plt.show()

# Boxplot for POW_ON_TIME
plt.figure(figsize=(8, 6))
plt.boxplot(data['POW_ON_TIME'], vert=False, sym='b.')
plt.title('Boxplot of POW_ON_TIME')
plt.xlabel('POW_ON_TIME values')
plt.tight_layout()
plt.show()

# Boxplot for TAPPING_TIME
plt.figure(figsize=(8, 6))
plt.boxplot(data['TAPPING_TIME'], vert=False, sym='b.')
plt.title('Boxplot of TAPPING_TIME')
plt.xlabel('TAPPING_TIME values')
plt.tight_layout()
plt.show()

# Boxplot for AR... (assuming the list continues)
plt.figure(figsize=(8, 6))
plt.boxplot(data['ARCING_TIME'], vert=False, sym='b.')
plt.title('Boxplot of AR...')
plt.xlabel('AR... values')
plt.tight_layout()
plt.show()


# Boxplot for DOWN_TIME
plt.figure(figsize=(8, 6))
plt.boxplot(data['DOWN_TIME'], vert=False, sym='b.')
plt.title('Boxplot of DOWN_TIME')
plt.xlabel('DOWN_TIME values')
plt.tight_layout()
plt.show()

# Boxplot for E1_CUR
plt.figure(figsize=(8, 6))
plt.boxplot(data['E1_CUR'], vert=False, sym='b.')
plt.title('Boxplot of E1_CUR')
plt.xlabel('E1_CUR values')
plt.tight_layout()
plt.show()

# Boxplot for E2_CUR
plt.figure(figsize=(8, 6))
plt.boxplot(data['E2_CUR'], vert=False, sym='b.')
plt.title('Boxplot of E2_CUR')
plt.xlabel('E2_CUR values')
plt.tight_layout()
plt.show()

# Boxplot for E3_CUR
plt.figure(figsize=(8, 6))
plt.boxplot(data['E3_CUR'], vert=False, sym='b.')
plt.title('Boxplot of E3_CUR')
plt.xlabel('E3_CUR values')
plt.tight_layout()
plt.show()

# Boxplot for SPOUT
plt.figure(figsize=(8, 6))
plt.boxplot(data['SPOUT'], vert=False, sym='b.')
plt.title('Boxplot of SPOUT')
plt.xlabel('SPOUT values')
plt.tight_layout()
plt.show()

# Boxplot for DOLOMIT
plt.figure(figsize=(8, 6))
plt.boxplot(data['DOLOMIT'], vert=False, sym='b.')
plt.title('Boxplot of DOLOMIT')
plt.xlabel('DOLOMIT values')
plt.tight_layout()
plt.show()

# Boxplot for CPC
plt.figure(figsize=(8, 6))
plt.boxplot(data['CPC'], vert=False, sym='b.')
plt.title('Boxplot of CPC')
plt.xlabel('CPC values')
plt.tight_layout()
plt.show()

# Boxplot for TEMPERATURE
plt.figure(figsize=(8, 6))
plt.boxplot(data['TEMPERATURE'], vert=False, sym='b.')
plt.title('Boxplot of TEMPERATURE')
plt.xlabel('TEMPERATURE values')
plt.tight_layout()
plt.show()

# Boxplot for POWER
plt.figure(figsize=(8, 6))
plt.boxplot(data['POWER'], vert=False, sym='b.')
plt.title('Boxplot of POWER')
plt.xlabel('POWER values')
plt.tight_layout()
plt.show()

# Boxplot for LAB_REP_TIME
plt.figure(figsize=(8, 6))
plt.boxplot(data['LAB_REP_TIME'], vert=False, sym='b.')
plt.title('Boxplot of LAB_REP_TIME')
plt.xlabel('LAB_REP_TIME values')
plt.tight_layout()
plt.show()

# Boxplot for C
plt.figure(figsize=(8, 6))
plt.boxplot(data['C'], vert=False, sym='b.')
plt.title('Boxplot of C')
plt.xlabel('C values')
plt.tight_layout()
plt.show()

# Boxplot for SI
plt.figure(figsize=(8, 6))
plt.boxplot(data['SI'], vert=False, sym='b.')
plt.title('Boxplot of SI')
plt.xlabel('SI values')
plt.tight_layout()
plt.show()


# Boxplot for MN column
plt.figure(figsize=(8, 6))
plt.boxplot(data['MN'], vert=False, sym='b.')
plt.title('Boxplot of MN')
plt.xlabel('MN values')
plt.tight_layout()
plt.show()


# Boxplot for P column
plt.figure(figsize=(8, 6))
plt.boxplot(data['P'], vert=False, sym='b.')
plt.title('Boxplot of P')
plt.xlabel('P values')
plt.tight_layout()
plt.show()

# Boxplot for S column
plt.figure(figsize=(8, 6))
plt.boxplot(data['S'], vert=False, sym='b.')
plt.title('Boxplot of S')
plt.xlabel('S values')
plt.tight_layout()
plt.show()

# Boxplot for CU
plt.figure(figsize=(8, 6))
plt.boxplot(data['CU'], vert=False, sym='b.')
plt.title('Boxplot of CU')
plt.xlabel('C values')
plt.tight_layout()
plt.show()


# CR
plt.figure(figsize=(8, 6))
plt.boxplot(data['CR'], vert=False, sym='b.')
plt.title('Boxplot of CR')
plt.xlabel('CR values')
plt.tight_layout()
plt.show()

# NI
plt.figure(figsize=(8, 6))
plt.boxplot(data['NI'], vert=False, sym='b.')
plt.title('Boxplot of NI')
plt.xlabel('NI values')
plt.tight_layout()
plt.show()

# N
plt.figure(figsize=(8, 6))
plt.boxplot(data['N'], vert=False, sym='b.')
plt.title('Boxplot of N')
plt.xlabel('N values')
plt.tight_layout()
plt.show()

# TIME_UTLN_PRCNT
plt.figure(figsize=(8, 6))
plt.boxplot(data['TIME_UTLN_PRCNT'], vert=False, sym='b.')
plt.title('Boxplot of TIME_UTLN_PRCNT')
plt.xlabel('TIME_UTLN_PRCNT values')
plt.tight_layout()
plt.show()

# TOP_COKE
plt.figure(figsize=(8, 6))
plt.boxplot(data['TOP_COKE'], vert=False, sym='b.')
plt.title('Boxplot of TOP_COKE')
plt.xlabel('TOP_COKE values')
plt.tight_layout()
plt.show()

# OPEN_C
plt.figure(figsize=(8, 6))
plt.boxplot(data['OPEN_C'], vert=False, sym='b.')
plt.title('Boxplot of OPEN_C')
plt.xlabel('OPEN_C values')
plt.tight_layout()
plt.show()

# TAP_C
plt.figure(figsize=(8, 6))
plt.boxplot(data['TAP_C'], vert=False, sym='b.')
plt.title('Boxplot of TAP_C')
plt.xlabel('TAP_C values')
plt.tight_layout()
plt.show()

# IT_KG
plt.figure(figsize=(8, 6))
plt.boxplot(data['IT_KG'], vert=False, sym='b.')
plt.title('Boxplot of IT_KG')
plt.xlabel('IT_KG values')
plt.tight_layout()
plt.show()

# BUCKET_NO
plt.figure(figsize=(8, 6))
plt.boxplot(data['BUCKET_NO'], vert=False, sym='b.')
plt.title('Boxplot of BUCKET_NO')
plt.xlabel('BUCKET_NO values')
plt.tight_layout()
plt.show()

# STATIC_WT
plt.figure(figsize=(8, 6))
plt.boxplot(data['STATIC_WT'], vert=False, sym='b.')
plt.title('Boxplot of STATIC_WT')
plt.xlabel('STATIC_WT values')
plt.tight_layout()
plt.show()

# LIME
plt.figure(figsize=(8, 6))
plt.boxplot(data['LIME'], vert=False, sym='b.')
plt.title('Boxplot of LIME')
plt.xlabel('LIME values')
plt.tight_layout()
plt.show()

# LIME2
plt.figure(figsize=(8, 6))
plt.boxplot(data['LIME2'], vert=False, sym='b.')
plt.title('Boxplot of LIME2')
plt.xlabel('LIME2 values')
plt.tight_layout()
plt.show()

# O2SIDE1
plt.figure(figsize=(8, 6))
plt.boxplot(data['O2SIDE1'], vert=False, sym='b.')
plt.title('Boxplot of O2SIDE1')
plt.xlabel('O2SIDE1 values')
plt.tight_layout()
plt.show()

# O2SIDE2
plt.figure(figsize=(8, 6))
plt.boxplot(data['O2SIDE2'], vert=False, sym='b.')
plt.title('Boxplot of O2SIDE2')
plt.xlabel('O2SIDE2 values')
plt.tight_layout()
plt.show()

# O2SIDE3
plt.figure(figsize=(8, 6))
plt.boxplot(data['O2SIDE3'], vert=False, sym='b.')
plt.title('Boxplot of O2SIDE3')
plt.xlabel('O2SIDE3 values')
plt.tight_layout()
plt.show()

# SPINNING
plt.figure(figsize=(8, 6))
plt.boxplot(data['SPINNING'], vert=False, sym='b.')
plt.title('Boxplot of SPINNING')
plt.xlabel('SPINNING values')
plt.tight_layout()
plt.show()

# RAMMING1
plt.figure(figsize=(8, 6))
plt.boxplot(data['RAMMING1'], vert=False, sym='b.')
plt.title('Boxplot of RAMMING1')
plt.xlabel('RAMMING1 values')
plt.tight_layout()
plt.show()

# RAMMING2
plt.figure(figsize=(8, 6))
plt.boxplot(data['RAMMING2'], vert=False, sym='b.')
plt.title('Boxplot of RAMMING2')
plt.xlabel('RAMMING2 values')
plt.tight_layout()
plt.show()

# PREV_TAP_TIME
plt.figure(figsize=(8, 6))
plt.boxplot(data['PREV_TAP_TIME'], vert=False, sym='b.')
plt.title('Boxplot of PREV_TAP_TIME')
plt.xlabel('PREV_TAP_TIME values')
plt.tight_layout()
plt.show()

# TAP_DURATION
plt.figure(figsize=(8, 6))
plt.boxplot(data['TAP_DURATION'], vert=False, sym='b.')
plt.title('Boxplot of TAP_DURATION')
plt.xlabel('TAP_DURATION values')
plt.tight_layout()
plt.show()

# Pour_Back_Metal
plt.figure(figsize=(8, 6))
plt.boxplot(data['Pour_Back_Metal'], vert=False, sym='b.')
plt.title('Boxplot of Pour_Back_Metal')
plt.xlabel('Pour_Back_Metal values')
plt.tight_layout()
plt.show()

# LM_WT
plt.figure(figsize=(8, 6))
plt.boxplot(data['LM_WT'], vert=False, sym='b.')
plt.title('Boxplot of LM_WT')
plt.xlabel('LM_WT values')
plt.tight_layout()
plt.show()

# Production
plt.figure(figsize=(8, 6))
plt.boxplot(data['Production'], vert=False, sym='b.')
plt.title('Boxplot of Production')
plt.xlabel('Production values')
plt.tight_layout()
plt.show()


#------------------------------------------------------------------------------------------------------------------
#Outlier Treatment
import pandas as pd
data = pd.read_csv(r"C:\Users\Admin\Desktop\C0DE\steeel.csv")
data.info

import numpy as np
import seaborn as sns


data.columns=data.columns.str.strip()

IQR = data['INJ1_QTY'].quantile(0.75) - data['INJ1_QTY'].quantile(0.25)

lower_limit = data['INJ1_QTY'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['INJ1_QTY'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['INJ1_QTY'] > upper_limit, upper_limit, np.where(data['INJ1_QTY'] < lower_limit, lower_limit, data['INJ1_QTY'])))
sns.boxplot(data.df_replaced)


IQR = data['INJ2_QTY'].quantile(0.75) - data['INJ2_QTY'].quantile(0.25)

lower_limit = data['INJ2_QTY'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['INJ2_QTY'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['INJ2_QTY'] > upper_limit, upper_limit, np.where(data['INJ2_QTY'] < lower_limit, lower_limit, data['INJ2_QTY'])))
sns.boxplot(data.df_replaced)

IQR = data['BSM'].quantile(0.75) - data['BSM'].quantile(0.25)

lower_limit = data['BSM'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['BSM'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['BSM'] > upper_limit, upper_limit, np.where(data['BSM'] < lower_limit, lower_limit, data['BSM'])))
sns.boxplot(data.df_replaced)

IQR = data['BP'].quantile(0.75) - data['BP'].quantile(0.25)

lower_limit = data['BP'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['BP'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['BP'] > upper_limit, upper_limit, np.where(data['BP'] < lower_limit, lower_limit, data['BP'])))
sns.boxplot(data.df_replaced)

IQR = data['HBI'].quantile(0.75) - data['HBI'].quantile(0.25)

lower_limit = data['HBI'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['HBI'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['HBI'] > upper_limit, upper_limit, np.where(data['HBI'] < lower_limit, lower_limit, data['HBI'])))
sns.boxplot(data.df_replaced)

IQR = data['OTHERS'].quantile(0.75) - data['OTHERS'].quantile(0.25)

lower_limit = data['OTHERS'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['OTHERS'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['OTHERS'] > upper_limit, upper_limit, np.where(data['OTHERS'] < lower_limit, lower_limit, data['OTHERS'])))
sns.boxplot(data.df_replaced)

#-------------------------------------------------------------------------------------------------

# For SCRAP_QTY
IQR = data['SCRAP_QTY'].quantile(0.75) - data['SCRAP_QTY'].quantile(0.25)
lower_limit = data['SCRAP_QTY'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['SCRAP_QTY'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['SCRAP_QTY'] > upper_limit, upper_limit, np.where(data['SCRAP_QTY'] < lower_limit, lower_limit, data['SCRAP_QTY'])))
sns.boxplot(data.df_replaced)

# For PIGIRON
IQR = data['PIGIRON'].quantile(0.75) - data['PIGIRON'].quantile(0.25)
lower_limit = data['PIGIRON'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['PIGIRON'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['PIGIRON'] > upper_limit, upper_limit, np.where(data['PIGIRON'] < lower_limit, lower_limit, data['PIGIRON'])))
sns.boxplot(data.df_replaced)

# For DRI1_QTY
IQR = data['DRI1_QTY'].quantile(0.75) - data['DRI1_QTY'].quantile(0.25)
lower_limit = data['DRI1_QTY'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['DRI1_QTY'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['DRI1_QTY'] > upper_limit, upper_limit, np.where(data['DRI1_QTY'] < lower_limit, lower_limit, data['DRI1_QTY'])))
sns.boxplot(data.df_replaced)

# For DRI2_QTY
IQR = data['DRI2_QTY'].quantile(0.75) - data['DRI2_QTY'].quantile(0.25)
lower_limit = data['DRI2_QTY'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['DRI2_QTY'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['DRI2_QTY'] > upper_limit, upper_limit, np.where(data['DRI2_QTY'] < lower_limit, lower_limit, data['DRI2_QTY'])))
sns.boxplot(data.df_replaced)

# For TOT_DRI_QTY
IQR = data['TOT_DRI_QTY'].quantile(0.75) - data['TOT_DRI_QTY'].quantile(0.25)
lower_limit = data['TOT_DRI_QTY'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['TOT_DRI_QTY'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['TOT_DRI_QTY'] > upper_limit, upper_limit, np.where(data['TOT_DRI_QTY'] < lower_limit, lower_limit, data['TOT_DRI_QTY'])))
sns.boxplot(data.df_replaced)

# For HOT_METAL
IQR = data['HOT_METAL'].quantile(0.75) - data['HOT_METAL'].quantile(0.25)
lower_limit = data['HOT_METAL'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['HOT_METAL'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['HOT_METAL'] > upper_limit, upper_limit, np.where(data['HOT_METAL'] < lower_limit, lower_limit, data['HOT_METAL'])))
sns.boxplot(data.df_replaced)

# For TotalCharge
IQR = data['TotalCharge'].quantile(0.75) - data['TotalCharge'].quantile(0.25)
lower_limit = data['TotalCharge'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['TotalCharge'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['TotalCharge'] > upper_limit, upper_limit, np.where(data['TotalCharge'] < lower_limit, lower_limit, data['TotalCharge'])))
sns.boxplot(data.df_replaced)

# For Hot_Heel
IQR = data['Hot_Heel'].quantile(0.75) - data['Hot_Heel'].quantile(0.25)
lower_limit = data['Hot_Heel'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['Hot_Heel'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['Hot_Heel'] > upper_limit, upper_limit, np.where(data['Hot_Heel'] < lower_limit, lower_limit, data['Hot_Heel'])))
sns.boxplot(data.df_replaced)

# For DOLO
IQR = data['DOLO'].quantile(0.75) - data['DOLO'].quantile(0.25)
lower_limit = data['DOLO'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['DOLO'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['DOLO'] > upper_limit, upper_limit, np.where(data['DOLO'] < lower_limit, lower_limit, data['DOLO'])))
sns.boxplot(data.df_replaced)

# For DOLO1_EMPTY
IQR = data['DOLO1_EMPTY'].quantile(0.75) - data['DOLO1_EMPTY'].quantile(0.25)
lower_limit = data['DOLO1_EMPTY'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['DOLO1_EMPTY'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['DOLO1_EMPTY'] > upper_limit, upper_limit, np.where(data['DOLO1_EMPTY'] < lower_limit, lower_limit, data['DOLO1_EMPTY'])))
sns.boxplot(data.df_replaced)

# For TOT_LIME_QTY
IQR = data['TOT_LIME_QTY'].quantile(0.75) - data['TOT_LIME_QTY'].quantile(0.25)
lower_limit = data['TOT_LIME_QTY'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['TOT_LIME_QTY'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['TOT_LIME_QTY'] > upper_limit, upper_limit, np.where(data['TOT_LIME_QTY'] < lower_limit, lower_limit, data['TOT_LIME_QTY'])))
sns.boxplot(data.df_replaced)

# For TAP_TEMP
IQR = data['TAP_TEMP'].quantile(0.75) - data['TAP_TEMP'].quantile(0.25)
lower_limit = data['TAP_TEMP'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['TAP_TEMP'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['TAP_TEMP'] > upper_limit, upper_limit, np.where(data['TAP_TEMP'] < lower_limit, lower_limit, data['TAP_TEMP'])))
sns.boxplot(data.df_replaced)

# For O2ACT
IQR = data['O2ACT'].quantile(0.75) - data['O2ACT'].quantile(0.25)
lower_limit = data['O2ACT'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['O2ACT'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['O2ACT'] > upper_limit, upper_limit, np.where(data['O2ACT'] < lower_limit, lower_limit, data['O2ACT'])))
sns.boxplot(data.df_replaced)

# For ENERGY
IQR = data['ENERGY'].quantile(0.75) - data['ENERGY'].quantile(0.25)
lower_limit = data['ENERGY'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['ENERGY'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['ENERGY'] > upper_limit, upper_limit, np.where(data['ENERGY'] < lower_limit, lower_limit, data['ENERGY'])))
sns.boxplot(data.df_replaced)

# For KWH_PER_TON
IQR = data['KWH_PER_TON'].quantile(0.75) - data['KWH_PER_TON'].quantile(0.25)
lower_limit = data['KWH_PER_TON'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['KWH_PER_TON'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['KWH_PER_TON'] > upper_limit, upper_limit, np.where(data['KWH_PER_TON'] < lower_limit, lower_limit, data['KWH_PER_TON'])))
sns.boxplot(data.df_replaced)

# For KWH_PER_MIN
IQR = data['KWH_PER_MIN'].quantile(0.75) - data['KWH_PER_MIN'].quantile(0.25)
lower_limit = data['KWH_PER_MIN'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['KWH_PER_MIN'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['KWH_PER_MIN'] > upper_limit, upper_limit, np.where(data['KWH_PER_MIN'] < lower_limit, lower_limit, data['KWH_PER_MIN'])))
sns.boxplot(data.df_replaced)

# For MELT_TIME
IQR = data['MELT_TIME'].quantile(0.75) - data['MELT_TIME'].quantile(0.25)
lower_limit = data['MELT_TIME'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['MELT_TIME'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['MELT_TIME'] > upper_limit, upper_limit, np.where(data['MELT_TIME'] < lower_limit, lower_limit, data['MELT_TIME'])))
sns.boxplot(data.df_replaced)

# For TA_TIME
IQR = data['TA_TIME'].quantile(0.75) - data['TA_TIME'].quantile(0.25)
lower_limit = data['TA_TIME'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['TA_TIME'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['TA_TIME'] > upper_limit, upper_limit, np.where(data['TA_TIME'] < lower_limit, lower_limit, data['TA_TIME'])))
sns.boxplot(data.df_replaced)

# For TT_TIME
IQR = data['TT_TIME'].quantile(0.75) - data['TT_TIME'].quantile(0.25)
lower_limit = data['TT_TIME'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['TT_TIME'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['TT_TIME'] > upper_limit, upper_limit, np.where(data['TT_TIME'] < lower_limit, lower_limit, data['TT_TIME'])))
sns.boxplot(data.df_replaced)

# For E1_CUR
IQR = data['E1_CUR'].quantile(0.75) - data['E1_CUR'].quantile(0.25)
lower_limit = data['E1_CUR'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['E1_CUR'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['E1_CUR'] > upper_limit, upper_limit, np.where(data['E1_CUR'] < lower_limit, lower_limit, data['E1_CUR'])))
sns.boxplot(data.df_replaced)

# For E2_CUR
IQR = data['E2_CUR'].quantile(0.75) - data['E2_CUR'].quantile(0.25)
lower_limit = data['E2_CUR'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['E2_CUR'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['E2_CUR'] > upper_limit, upper_limit, np.where(data['E2_CUR'] < lower_limit, lower_limit, data['E2_CUR'])))
sns.boxplot(data.df_replaced)

# For E3_CUR
IQR = data['E3_CUR'].quantile(0.75) - data['E3_CUR'].quantile(0.25)
lower_limit = data['E3_CUR'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['E3_CUR'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['E3_CUR'] > upper_limit, upper_limit, np.where(data['E3_CUR'] < lower_limit, lower_limit, data['E3_CUR'])))
sns.boxplot(data.df_replaced)

# For SPOUT
IQR = data['SPOUT'].quantile(0.75) - data['SPOUT'].quantile(0.25)
lower_limit = data['SPOUT'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['SPOUT'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['SPOUT'] > upper_limit, upper_limit, np.where(data['SPOUT'] < lower_limit, lower_limit, data['SPOUT'])))
sns.boxplot(data.df_replaced)

# For C
IQR = data['C'].quantile(0.75) - data['C'].quantile(0.25)
lower_limit = data['C'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['C'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['C'] > upper_limit, upper_limit, np.where(data['C'] < lower_limit, lower_limit, data['C'])))
sns.boxplot(data.df_replaced)

# For SI
IQR = data['SI'].quantile(0.75) - data['SI'].quantile(0.25)
lower_limit = data['SI'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['SI'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['SI'] > upper_limit, upper_limit, np.where(data['SI'] < lower_limit, lower_limit, data['SI'])))
sns.boxplot(data.df_replaced)

# For MN
IQR = data['MN'].quantile(0.75) - data['MN'].quantile(0.25)
lower_limit = data['MN'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['MN'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['MN'] > upper_limit, upper_limit, np.where(data['MN'] < lower_limit, lower_limit, data['MN'])))
sns.boxplot(data.df_replaced)

# For P
IQR = data['P'].quantile(0.75) - data['P'].quantile(0.25)
lower_limit = data['P'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['P'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['P'] > upper_limit, upper_limit, np.where(data['P'] < lower_limit, lower_limit, data['P'])))
sns.boxplot(data.df_replaced)

# For S
IQR = data['S'].quantile(0.75) - data['S'].quantile(0.25)
lower_limit = data['S'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['S'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['S'] > upper_limit, upper_limit, np.where(data['S'] < lower_limit, lower_limit, data['S'])))
sns.boxplot(data.df_replaced)

# For CU
IQR = data['CU'].quantile(0.75) - data['CU'].quantile(0.25)
lower_limit = data['CU'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['CU'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['CU'] > upper_limit, upper_limit, np.where(data['CU'] < lower_limit, lower_limit, data['CU'])))
sns.boxplot(data.df_replaced)

# For CR
IQR = data['CR'].quantile(0.75) - data['CR'].quantile(0.25)
lower_limit = data['CR'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['CR'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['CR'] > upper_limit, upper_limit, np.where(data['CR'] < lower_limit, lower_limit, data['CR'])))
sns.boxplot(data.df_replaced)

# For TAP_C
IQR = data['TAP_C'].quantile(0.75) - data['TAP_C'].quantile(0.25)
lower_limit = data['TAP_C'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['TAP_C'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['TAP_C'] > upper_limit, upper_limit, np.where(data['TAP_C'] < lower_limit, lower_limit, data['TAP_C'])))
sns.boxplot(data.df_replaced)

# For IT_KG
IQR = data['IT_KG'].quantile(0.75) - data['IT_KG'].quantile(0.25)
lower_limit = data['IT_KG'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['IT_KG'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['IT_KG'] > upper_limit, upper_limit, np.where(data['IT_KG'] < lower_limit, lower_limit, data['IT_KG'])))
sns.boxplot(data.df_replaced)

# For BUCKET_NO
IQR = data['BUCKET_NO'].quantile(0.75) - data['BUCKET_NO'].quantile(0.25)
lower_limit = data['BUCKET_NO'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['BUCKET_NO'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['BUCKET_NO'] > upper_limit, upper_limit, np.where(data['BUCKET_NO'] < lower_limit, lower_limit, data['BUCKET_NO'])))
sns.boxplot(data.df_replaced)

# For STATIC_WT
IQR = data['STATIC_WT'].quantile(0.75) - data['STATIC_WT'].quantile(0.25)
lower_limit = data['STATIC_WT'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['STATIC_WT'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['STATIC_WT'] > upper_limit, upper_limit, np.where(data['STATIC_WT'] < lower_limit, lower_limit, data['STATIC_WT'])))
sns.boxplot(data.df_replaced)

# For LIME
IQR = data['LIME'].quantile(0.75) - data['LIME'].quantile(0.25)
lower_limit = data['LIME'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['LIME'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['LIME'] > upper_limit, upper_limit, np.where(data['LIME'] < lower_limit, lower_limit, data['LIME'])))
sns.boxplot(data.df_replaced)

# For LIME2
IQR = data['LIME2'].quantile(0.75) - data['LIME2'].quantile(0.25)
lower_limit = data['LIME2'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['LIME2'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['LIME2'] > upper_limit, upper_limit, np.where(data['LIME2'] < lower_limit, lower_limit, data['LIME2'])))
sns.boxplot(data.df_replaced)

# For O2SIDE1
IQR = data['O2SIDE1'].quantile(0.75) - data['O2SIDE1'].quantile(0.25)
lower_limit = data['O2SIDE1'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['O2SIDE1'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['O2SIDE1'] > upper_limit, upper_limit, np.where(data['O2SIDE1'] < lower_limit, lower_limit, data['O2SIDE1'])))
sns.boxplot(data.df_replaced)

# For O2SIDE2
IQR = data['O2SIDE2'].quantile(0.75) - data['O2SIDE2'].quantile(0.25)
lower_limit = data['O2SIDE2'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['O2SIDE2'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['O2SIDE2'] > upper_limit, upper_limit, np.where(data['O2SIDE2'] < lower_limit, lower_limit, data['O2SIDE2'])))
sns.boxplot(data.df_replaced)

# For O2SIDE3
IQR = data['O2SIDE3'].quantile(0.75) - data['O2SIDE3'].quantile(0.25)
lower_limit = data['O2SIDE3'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['O2SIDE3'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['O2SIDE3'] > upper_limit, upper_limit, np.where(data['O2SIDE3'] < lower_limit, lower_limit, data['O2SIDE3'])))
sns.boxplot(data.df_replaced)

# For SPINNING
IQR = data['SPINNING'].quantile(0.75) - data['SPINNING'].quantile(0.25)
lower_limit = data['SPINNING'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['SPINNING'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['SPINNING'] > upper_limit, upper_limit, np.where(data['SPINNING'] < lower_limit, lower_limit, data['SPINNING'])))
sns.boxplot(data.df_replaced)

# For RAMMING1
IQR = data['RAMMING1'].quantile(0.75) - data['RAMMING1'].quantile(0.25)
lower_limit = data['RAMMING1'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['RAMMING1'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['RAMMING1'] > upper_limit, upper_limit, np.where(data['RAMMING1'] < lower_limit, lower_limit, data['RAMMING1'])))
sns.boxplot(data.df_replaced)

# For RAMMING2
IQR = data['RAMMING2'].quantile(0.75) - data['RAMMING2'].quantile(0.25)
lower_limit = data['RAMMING2'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['RAMMING2'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['RAMMING2'] > upper_limit, upper_limit, np.where(data['RAMMING2'] < lower_limit, lower_limit, data['RAMMING2'])))
sns.boxplot(data.df_replaced)

# For TAP_DURATION
IQR = data['TAP_DURATION'].quantile(0.75) - data['TAP_DURATION'].quantile(0.25)
lower_limit = data['TAP_DURATION'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['TAP_DURATION'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['TAP_DURATION'] > upper_limit, upper_limit, np.where(data['TAP_DURATION'] < lower_limit, lower_limit, data['TAP_DURATION'])))
sns.boxplot(data.df_replaced)


# For Pour_Back_Metal
IQR = data['Pour_Back_Metal'].quantile(0.75) - data['Pour_Back_Metal'].quantile(0.25)
lower_limit = data['Pour_Back_Metal'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['Pour_Back_Metal'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['Pour_Back_Metal'] > upper_limit, upper_limit, np.where(data['Pour_Back_Metal'] < lower_limit, lower_limit, data['Pour_Back_Metal'])))
sns.boxplot(data.df_replaced)

# For LM_WT
IQR = data['LM_WT'].quantile(0.75) - data['LM_WT'].quantile(0.25)
lower_limit = data['LM_WT'].quantile(0.25) - (IQR * 1.5)
upper_limit = data['LM_WT'].quantile(0.75) + (IQR * 1.5)
data['df_replaced'] = pd.DataFrame(np.where(data['LM_WT'] > upper_limit, upper_limit, np.where(data['LM_WT'] < lower_limit, lower_limit, data['LM_WT'])))
sns.boxplot(data.df_replaced)



#-===========================================================================================================================================
#Zero & near Zero Variance features

import pandas as pd

# Assume df is your pandas DataFrame with your data
# Replace 'your_data.csv' with your actual data source
data = pd.read_csv(r"C:\Users\Admin\Desktop\C0DE\steeel.csv")
data = pd.read_csv(r"C:\Users\Admin\Desktop\C0DE\steeel.csv")
# Example for 'INJ1_QTY' column
variance_inj1_qty = data['INJ1_QTY'].var()
print(f"Variance of 'INJ1_QTY': {variance_inj1_qty}")

# Example for 'INJ2_QTY' column
variance_inj2_qty = data['INJ2_QTY'].var()
print(f"Variance of 'INJ2_QTY': {variance_inj2_qty}")

# Example for 'BSM' column
variance_bsm = data['BSM'].var()
print(f"Variance of 'BSM': {variance_bsm}")

# Example for 'TP' column
variance_tp = data['TP'].var()
print(f"Variance of 'TP': {variance_tp}")

# Example for 'MSTB' column
variance_mstb = data['MSTB'].var()
print(f"Variance of 'MSTB': {variance_mstb}")

# Example for 'SKULL' column
variance_skull = data['SKULL'].var()
print(f"Variance of 'SKULL': {variance_skull}")

# Example for 'SHRAD' column
variance_shrad = data['SHRAD'].var()
print(f"Variance of 'SHRAD': {variance_shrad}")

# Example for 'REMET' column
variance_remet = data['REMET'].var()
print(f"Variance of 'REMET': {variance_remet}")

# Example for 'BP' column
variance_bp = data['BP'].var()
print(f"Variance of 'BP': {variance_bp}")

# Example for 'HBI' column
variance_hbi = data['HBI'].var()
print(f"Variance of 'HBI': {variance_hbi}")

# Example for 'OTHERS' column
variance_others = data['OTHERS'].var()
print(f"Variance of 'OTHERS': {variance_others}")

# Example for 'SCRAP_QTY' column
variance_scrap_qty = data['SCRAP_QTY'].var()
print(f"Variance of 'SCRAP_QTY': {variance_scrap_qty}")

# Example for 'PIGIRON' column
variance_pigiron = data['PIGIRON'].var()
print(f"Variance of 'PIGIRON': {variance_pigiron}")

# Example for 'DRI1_QTY' column
variance_dri1_qty = data['DRI1_QTY'].var()
print(f"Variance of 'DRI1_QTY': {variance_dri1_qty}")

# Example for 'DRI2_QTY' column
variance_dri2_qty = data['DRI2_QTY'].var()
print(f"Variance of 'DRI2_QTY': {variance_dri2_qty}")

# Example for 'TOT_DRI_QTY' column
variance_tot_dri_qty = data['TOT_DRI_QTY'].var()
print(f"Variance of 'TOT_DRI_QTY': {variance_tot_dri_qty}")

# Example for 'HOT_METAL' column
variance_hot_metal = data['HOT_METAL'].var()
print(f"Variance of 'HOT_METAL': {variance_hot_metal}")

# Example for 'Total_Charge' column
variance_total_charge = data['Total_Charge'].var()
print(f"Variance of 'Total_Charge': {variance_total_charge}")

# Example for 'Hot_Heel' column
variance_hot_heel = data['Hot_Heel'].var()
print(f"Variance of 'Hot_Heel': {variance_hot_heel}")

# Example for 'DOLO' column
variance_dolo = data['DOLO'].var()
print(f"Variance of 'DOLO': {variance_dolo}")

# Example for 'DOLO1_EMPTY' column
variance_dolo1_empty = data['DOLO1_EMPTY'].var()
print(f"Variance of 'DOLO1_EMPTY': {variance_dolo1_empty}")

# Example for 'TOT_LIME_QTY' column
variance_tot_lime_qty = data['TOT_LIME_QTY'].var()
print(f"Variance of 'TOT_LIME_QTY': {variance_tot_lime_qty}")

# Example for 'TAP_TEMP' column
variance_tap_temp = data['TAP_TEMP'].var()
print(f"Variance of 'TAP_TEMP': {variance_tap_temp}")

# Example for 'O2REQ' column
variance_o2req = data['O2REQ'].var()
print(f"Variance of 'O2REQ': {variance_o2req}")

# Example for 'O2ACT' column
variance_o2act = data['O2ACT'].var()
print(f"Variance of 'O2ACT': {variance_o2act}")

# Example for 'ENERGY' column
variance_energy = data['ENERGY'].var()
print(f"Variance of 'ENERGY': {variance_energy}")

# Example for 'KWH_PER_TON' column
variance_kwh_per_ton = data['KWH_PER_TON'].var()
print(f"Variance of 'KWH_PER_TON': {variance_kwh_per_ton}")

# Example for 'KWH_PER_MIN' column
variance_kwh_per_min = data['KWH_PER_MIN'].var()
print(f"Variance of 'KWH_PER_MIN': {variance_kwh_per_min}")

# Example for 'MELT_TIME' column
variance_melt_time = data['MELT_TIME'].var()
print(f"Variance of 'MELT_TIME': {variance_melt_time}")

# Example for 'TA_TIME' column
variance_ta_time = data['TA_TIME'].var()
print(f"Variance of 'TA_TIME': {variance_ta_time}")

# Example for 'TT_TIME' column
variance_tt_time = data['TT_TIME'].var()
print(f"Variance of 'TT_TIME': {variance_tt_time}")

# Example for 'POW_ON_TIME' column
variance_pow_on_time = data['POW_ON_TIME'].var()
print(f"Variance of 'POW_ON_TIME': {variance_pow_on_time}")

# Example for 'TAPPING_TIME' column
variance_tapping_time = data['TAPPING_TIME'].var()
print(f"Variance of 'TAPPING_TIME': {variance_tapping_time}")

# Example for 'ARCING_TIME' column
variance_arcing_time = data['ARCING_TIME'].var()
print(f"Variance of 'ARCING_TIME': {variance_arcing_time}")

# Example for 'DOWN_TIME' column
variance_down_time = data['DOWN_TIME'].var()
print(f"Variance of 'DOWN_TIME': {variance_down_time}")

# Example for 'E1_CUR' column
variance_e1_cur = data['E1_CUR'].var()
print(f"Variance of 'E1_CUR': {variance_e1_cur}")

# Example for 'E2_CUR' column
variance_e2_cur = data['E2_CUR'].var()
print(f"Variance of 'E2_CUR': {variance_e2_cur}")

# Example for 'E3_CUR' column
variance_e3_cur = data['E3_CUR'].var()
print(f"Variance of 'E3_CUR': {variance_e3_cur}")

# Example for 'SPOUT' column
variance_spout = data['SPOUT'].var()
print(f"Variance of 'SPOUT': {variance_spout}")

# Example for 'DOLOMIT' column
variance_dolomit = data['DOLOMIT'].var()
print(f"Variance of 'DOLOMIT': {variance_dolomit}")

# Example for 'CPC' column
variance_cpc = data['CPC'].var()
print(f"Variance of 'CPC': {variance_cpc}")

# Example for 'TEMPERATURE' column
variance_temperature = data['TEMPERATURE'].var()
print(f"Variance of 'TEMPERATURE': {variance_temperature}")

# Example for 'POWER' column
variance_power =data['POWER'].var()
print(f"Variance of 'POWER': {variance_power}")

# Example for 'C' column
variance_c = data['C'].var()
print(f"Variance of 'C': {variance_c}")

# Example for 'SI' column
variance_si = data['SI'].var()
print(f"Variance of 'SI': {variance_si}")

# Example for 'MN' column
variance_mn = data['MN'].var()
print(f"Variance of 'MN': {variance_mn}")

# Example for 'P' column
variance_p = data['P'].var()
print(f"Variance of 'P': {variance_p}")

# Example for 'S' column
variance_s = data['S'].var()
print(f"Variance of 'S': {variance_s}")

# Example for 'CU' column
variance_cu = data['CU'].var()
print(f"Variance of 'CU': {variance_cu}")

# Example for 'CR' column
variance_cr = data['CR'].var()
print(f"Variance of 'CR': {variance_cr}")

# Example for 'NI' column
variance_ni = data['NI'].var()
print(f"Variance of 'NI': {variance_ni}")

# Example for 'N' column
variance_n = data['N'].var()
print(f"Variance of 'N': {variance_n}")

# Example for 'TIME_UTLN_PRCNT' column
variance_time_utln_prcnt = data['TIME_UTLN_PRCNT'].var()
print(f"Variance of 'TIME_UTLN_PRCNT': {variance_time_utln_prcnt}")

# Example for 'TOP_COKE' column
variance_top_coke = data['TOP_COKE'].var()
print(f"Variance of 'TOP_COKE': {variance_top_coke}")

# Example for 'OPEN_C' column
variance_open_c = data['OPEN_C'].var()
print(f"Variance of 'OPEN_C': {variance_open_c}")

# Example for 'TAP_C' column
variance_tap_c = data['TAP_C'].var()
print(f"Variance of 'TAP_C': {variance_tap_c}")

# Example for 'IT_KG' column
variance_it_kg = data['IT_KG'].var()
print(f"Variance of 'IT_KG': {variance_it_kg}")

# Example for 'BUCKET_NO' column
variance_bucket_no = data['BUCKET_NO'].var()
print(f"Variance of 'BUCKET_NO': {variance_bucket_no}")

# Example for 'STATIC_WT' column
variance_static_wt = data['STATIC_WT'].var()
print(f"Variance of 'STATIC_WT': {variance_static_wt}")

# Example for 'LIME' column
variance_lime = data['LIME'].var()
print(f"Variance of 'LIME': {variance_lime}")

# Example for 'LIME2' column
variance_lime2 = data['LIME2'].var()
print(f"Variance of 'LIME2': {variance_lime2}")

# Example for 'O2SIDE1' column
variance_o2side1 = data['O2SIDE1'].var()
print(f"Variance of 'O2SIDE1': {variance_o2side1}")

# Example for 'O2SIDE2' column
variance_o2side2 = data['O2SIDE2'].var()
print(f"Variance of 'O2SIDE2': {variance_o2side2}")

# Example for 'O2SIDE3' column
variance_o2side3 = data['O2SIDE3'].var()
print(f"Variance of 'O2SIDE3': {variance_o2side3}")

# Example for 'SPINNING' column
variance_spinning = data['SPINNING'].var()
print(f"Variance of 'SPINNING': {variance_spinning}")

# Example for 'RAMMING1' column
variance_ramming1 = data['RAMMING1'].var()
print(f"Variance of 'RAMMING1': {variance_ramming1}")

# Example for 'RAMMING2' column
variance_ramming2 = data['RAMMING2'].var()
print(f"Variance of 'RAMMING2': {variance_ramming2}")

# Example for 'PREV_TAP_TIME' column
variance_prev_tap_time = data['PREV_TAP_TIME'].var()
print(f"Variance of 'PREV_TAP_TIME': {variance_prev_tap_time}")

# Example for 'TAP_DURATION' column
variance_tap_duration = data['TAP_DURATION'].var()
print(f"Variance of 'TAP_DURATION': {variance_tap_duration}")

# Example for 'Pour_Back_Metal' column
variance_pour_back_metal = data['Pour_Back_Metal'].var()
print(f"Variance of 'Pour_Back_Metal': {variance_pour_back_metal}")

# Example for 'LM_WT' column
variance_lm_wt = data['LM_WT'].var()
print(f"Variance of 'LM_WT': {variance_lm_wt}")

# Example for 'Production' column
variance_production = data['Production'].var()
print(f"Variance of 'Production': {variance_production}")


#==============================================================================================================

#Missing Values
data.dropna(inplace = True)
print(data)

#==============================================================================================================

#Graphical Representation
#histogram


import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r"C:\Users\Admin\Desktop\C0DE\steeel.csv")

plt.figure(figsize=(10, 6))


# Plotting the specified column (INJ1_QTY)
plt.hist(data['INJ1_QTY'], bins=20)
plt.title('Histogram of INJ1_QTY')
plt.xlabel('INJ1_QTY values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

# Plotting the specified column (INJ2_QTY)
plt.hist(data['INJ2_QTY'], bins=20)
plt.title('Histogram of INJ2_QTY')
plt.xlabel('INJ2_QTY values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

# Plotting the specified column (BSM)
plt.hist(data['BSM'], bins=20)
plt.title('Histogram of BSM')
plt.xlabel('BSM values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

# Plotting the specified column (TP)
plt.hist(data['TP'], bins=20)
plt.title('Histogram of TP')
plt.xlabel('TP values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

# Plotting the specified column (MSTB)
plt.hist(data['MSTB'], bins=20)
plt.title('Histogram of MSTB')
plt.xlabel('MSTB values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

# Plotting the specified column (SKULL)
plt.hist(data['SKULL'], bins=20)
plt.title('Histogram of SKULL')
plt.xlabel('SKULL values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

# Plotting the specified column (SHRAD)
plt.hist(data['SHRAD'], bins=20)
plt.title('Histogram of SHRAD')
plt.xlabel('SHRAD values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

# Plotting the specified column (REMET)
plt.hist(data['REMET'], bins=20)
plt.title('Histogram of REMET')
plt.xlabel('REMET values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()



# BP
plt.figure(figsize=(10, 6))
plt.hist(data['BP'], bins=20)
plt.title('Histogram of BP')
plt.xlabel('BP values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# HBI
plt.figure(figsize=(10, 6))
plt.hist(data['HBI'], bins=20)
plt.title('Histogram of HBI')
plt.xlabel('HBI values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# OTHERS
plt.figure(figsize=(10, 6))
plt.hist(data['OTHERS'], bins=20)
plt.title('Histogram of OTHERS')
plt.xlabel('OTHERS values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# SCRAP_QTY
plt.figure(figsize=(10, 6))
plt.hist(data['SCRAP_QTY'], bins=20)
plt.title('Histogram of SCRAP_QTY')
plt.xlabel('SCRAP_QTY values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# PIGIRON
plt.figure(figsize=(10, 6))
plt.hist(data['PIGIRON'], bins=20)
plt.title('Histogram of PIGIRON')
plt.xlabel('PIGIRON values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# DRI1_QTY
plt.figure(figsize=(10, 6))
plt.hist(data['DRI1_QTY'], bins=20)
plt.title('Histogram of DRI1_QTY')
plt.xlabel('DRI1_QTY values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# DRI2_QTY
plt.figure(figsize=(10, 6))
plt.hist(data['DRI2_QTY'], bins=20)
plt.title('Histogram of DRI2_QTY')
plt.xlabel('DRI2_QTY values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TOT_DRI_QTY
plt.figure(figsize=(10, 6))
plt.hist(data['TOT_DRI_QTY'], bins=20)
plt.title('Histogram of TOT_DRI_QTY')
plt.xlabel('TOT_DRI_QTY values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# HOT_METAL
plt.figure(figsize=(10, 6))
plt.hist(data['HOT_METAL'], bins=20)
plt.title('Histogram of HOT_METAL')
plt.xlabel('HOT_METAL values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TotalCharge
plt.figure(figsize=(10, 6))
plt.hist(data['TotalCharge'], bins=20)
plt.title('Histogram of TotalCharge')
plt.xlabel('TotalCharge values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Hot_Heel
plt.figure(figsize=(10, 6))
plt.hist(data['Hot_Heel'], bins=20)
plt.title('Histogram of Hot_Heel')
plt.xlabel('Hot_Heel values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# DOLO
plt.figure(figsize=(10, 6))
plt.hist(data['DOLO'], bins=20)
plt.title('Histogram of DOLO')
plt.xlabel('DOLO values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# DOLO1_EMPTY
plt.figure(figsize=(10, 6))
plt.hist(data['DOLO1_EMPTY'], bins=20)
plt.title('Histogram of DOLO1_EMPTY')
plt.xlabel('DOLO1_EMPTY values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TOT_LIME_QTY
plt.figure(figsize=(10, 6))
plt.hist(data['TOT_LIME_QTY'], bins=20)
plt.title('Histogram of TOT_LIME_QTY')
plt.xlabel('TOT_LIME_QTY values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TAP_TEMP
plt.figure(figsize=(10, 6))
plt.hist(data['TAP_TEMP'], bins=20)
plt.title('Histogram of TAP_TEMP')
plt.xlabel('TAP_TEMP values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# O2REQ
plt.figure(figsize=(10, 6))
plt.hist(data['O2REQ'], bins=20)
plt.title('Histogram of O2REQ')
plt.xlabel('O2REQ values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# O2ACT
plt.figure(figsize=(10, 6))
plt.hist(data['O2ACT'], bins=20)
plt.title('Histogram of O2ACT')
plt.xlabel('O2ACT values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ENERGY
plt.figure(figsize=(10, 6))
plt.hist(data['ENERGY'], bins=20)
plt.title('Histogram of ENERGY')
plt.xlabel('ENERGY values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# KWH_PER_TON
plt.figure(figsize=(10, 6))
plt.hist(data['KWH_PER_TON'], bins=20)
plt.title('Histogram of KWH_PER_TON')
plt.xlabel('KWH_PER_TON values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# KWH_PER_MIN
plt.figure(figsize=(10, 6))
plt.hist(data['KWH_PER_MIN'], bins=20)
plt.title('Histogram of KWH_PER_MIN')
plt.xlabel('KWH_PER_MIN values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# MELT_TIME
plt.figure(figsize=(10, 6))
plt.hist(data['MELT_TIME'], bins=20)
plt.title('Histogram of MELT_TIME')
plt.xlabel('MELT_TIME values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TA_TIME
plt.figure(figsize=(10, 6))
plt.hist(data['TA_TIME'], bins=20)
plt.title('Histogram of TA_TIME')
plt.xlabel('TA_TIME values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TT_TIME
plt.figure(figsize=(10, 6))
plt.hist(data['TT_TIME'], bins=20)
plt.title('Histogram of TT_TIME')
plt.xlabel('TT_TIME values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# POW_ON_TIME
plt.figure(figsize=(10, 6))
plt.hist(data['POW_ON_TIME'], bins=20)
plt.title('Histogram of POW_ON_TIME')
plt.xlabel('POW_ON_TIME values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TAPPING_TIME
plt.figure(figsize=(10, 6))
plt.hist(data['TAPPING_TIME'], bins=20)
plt.title('Histogram of TAPPING_TIME')
plt.xlabel('TAPPING_TIME values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# AR
plt.figure(figsize=(10, 6))
plt.hist(data['ARCING_TIME'], bins=20)
plt.title('Histogram of AR')
plt.xlabel('AR values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# DOWN_TIME
plt.figure(figsize=(10, 6))
plt.hist(data['DOWN_TIME'], bins=20)
plt.title('Histogram of DOWN_TIME')
plt.xlabel('DOWN_TIME values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# E1_CUR
plt.figure(figsize=(10, 6))
plt.hist(data['E1_CUR'], bins=20)
plt.title('Histogram of E1_CUR')
plt.xlabel('E1_CUR values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# E2_CUR
plt.figure(figsize=(10, 6))
plt.hist(data['E2_CUR'], bins=20)
plt.title('Histogram of E2_CUR')
plt.xlabel('E2_CUR values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# E3_CUR
plt.figure(figsize=(10, 6))
plt.hist(data['E3_CUR'], bins=20)
plt.title('Histogram of E3_CUR')
plt.xlabel('E3_CUR values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# SPOUT
plt.figure(figsize=(10, 6))
plt.hist(data['SPOUT'], bins=20)
plt.title('Histogram of SPOUT')
plt.xlabel('SPOUT values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# DOLOMIT
plt.figure(figsize=(10, 6))
plt.hist(data['DOLOMIT'], bins=20)
plt.title('Histogram of DOLOMIT')
plt.xlabel('DOLOMIT values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# CPC
plt.figure(figsize=(10, 6))
plt.hist(data['CPC'], bins=20)
plt.title('Histogram of CPC')
plt.xlabel('CPC values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TEMPERATURE
plt.figure(figsize=(10, 6))
plt.hist(data['TEMPERATURE'], bins=20)
plt.title('Histogram of TEMPERATURE')
plt.xlabel('TEMPERATURE values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# POWER
plt.figure(figsize=(10, 6))
plt.hist(data['POWER'], bins=20)
plt.title('Histogram of POWER')
plt.xlabel('POWER values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# LAB_REP_TIME
plt.figure(figsize=(10, 6))
plt.hist(data['LAB_REP_TIME'], bins=20)
plt.title('Histogram of LAB_REP_TIME')
plt.xlabel('LAB_REP_TIME values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# C
plt.figure(figsize=(10, 6))
plt.hist(data['C'], bins=20)
plt.title('Histogram of C')
plt.xlabel('C values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# SI
plt.figure(figsize=(10, 6))
plt.hist(data['SI'], bins=20)
plt.title('Histogram of SI')
plt.xlabel('SI values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# MN
plt.figure(figsize=(10, 6))
plt.hist(data['MN'], bins=20)
plt.title('Histogram of MN')
plt.xlabel('MN values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# P
plt.figure(figsize=(10, 6))
plt.hist(data['P'], bins=20)
plt.title('Histogram of P')
plt.xlabel('P values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# S
plt.figure(figsize=(10, 6))
plt.hist(data['S'], bins=20)
plt.title('Histogram of S')
plt.xlabel('S values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# CU
plt.figure(figsize=(10, 6))
plt.hist(data['CU'], bins=20)
plt.title('Histogram of CU')
plt.xlabel('CU values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# CR
plt.figure(figsize=(10, 6))
plt.hist(data['CR'], bins=20)
plt.title('Histogram of CR')
plt.xlabel('CR values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# NI
plt.figure(figsize=(10, 6))
plt.hist(data['NI'], bins=20)
plt.title('Histogram of NI')
plt.xlabel('NI values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# N
plt.figure(figsize=(10, 6))
plt.hist(data['N'], bins=20)
plt.title('Histogram of N')
plt.xlabel('N values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TIME_UTLN_PRCNT
plt.figure(figsize=(10, 6))
plt.hist(data['TIME_UTLN_PRCNT'], bins=20)
plt.title('Histogram of TIME_UTLN_PRCNT')
plt.xlabel('TIME_UTLN_PRCNT values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TOP_COKE
plt.figure(figsize=(10, 6))
plt.hist(data['TOP_COKE'], bins=20)
plt.title('Histogram of TOP_COKE')
plt.xlabel('TOP_COKE values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# OPEN_C
plt.figure(figsize=(10, 6))
plt.hist(data['OPEN_C'], bins=20)
plt.title('Histogram of OPEN_C')
plt.xlabel('OPEN_C values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TAP_C
plt.figure(figsize=(10, 6))
plt.hist(data['TAP_C'], bins=20)
plt.title('Histogram of TAP_C')
plt.xlabel('TAP_C values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# IT_KG
plt.figure(figsize=(10, 6))
plt.hist(data['IT_KG'], bins=20)
plt.title('Histogram of IT_KG')
plt.xlabel('IT_KG values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# BUCKET_NO
plt.figure(figsize=(10, 6))
plt.hist(data['BUCKET_NO'], bins=20)
plt.title('Histogram of BUCKET_NO')
plt.xlabel('BUCKET_NO values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# STATIC_WT
plt.figure(figsize=(10, 6))
plt.hist(data['STATIC_WT'], bins=20)
plt.title('Histogram of STATIC_WT')
plt.xlabel('STATIC_WT values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# LIME
plt.figure(figsize=(10, 6))
plt.hist(data['LIME'], bins=20)
plt.title('Histogram of LIME')
plt.xlabel('LIME values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# LIME2
plt.figure(figsize=(10, 6))
plt.hist(data['LIME2'], bins=20)
plt.title('Histogram of LIME2')
plt.xlabel('LIME2 values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# O2SIDE1
plt.figure(figsize=(10, 6))
plt.hist(data['O2SIDE1'], bins=20)
plt.title('Histogram of O2SIDE1')
plt.xlabel('O2SIDE1 values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# O2SIDE2
plt.figure(figsize=(10, 6))
plt.hist(data['O2SIDE2'], bins=20)
plt.title('Histogram of O2SIDE2')
plt.xlabel('O2SIDE2 values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# O2SIDE3
plt.figure(figsize=(10, 6))
plt.hist(data['O2SIDE3'], bins=20)
plt.title('Histogram of O2SIDE3')
plt.xlabel('O2SIDE3 values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# SPINNING
plt.figure(figsize=(10, 6))
plt.hist(data['SPINNING'], bins=20)
plt.title('Histogram of SPINNING')
plt.xlabel('SPINNING values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# RAMMING1
plt.figure(figsize=(10, 6))
plt.hist(data['RAMMING1'], bins=20)
plt.title('Histogram of RAMMING1')
plt.xlabel('RAMMING1 values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# RAMMING2
plt.figure(figsize=(10, 6))
plt.hist(data['RAMMING2'], bins=20)
plt.title('Histogram of RAMMING2')
plt.xlabel('RAMMING2 values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# PREV_TAP_TIME
plt.figure(figsize=(10, 6))
plt.hist(data['PREV_TAP_TIME'], bins=20)
plt.title('Histogram of PREV_TAP_TIME')
plt.xlabel('PREV_TAP_TIME values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TAP_DURATION
plt.figure(figsize=(10, 6))
plt.hist(data['TAP_DURATION'], bins=20)
plt.title('Histogram of TAP_DURATION')
plt.xlabel('TAP_DURATION values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Pour_Back_Metal
plt.figure(figsize=(10, 6))
plt.hist(data['Pour_Back_Metal'], bins=20)
plt.title('Histogram of Pour_Back_Metal')
plt.xlabel('Pour_Back_Metal values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# LM_WT
plt.figure(figsize=(10, 6))
plt.hist(data['LM_WT'], bins=20)
plt.title('Histogram of LM_WT')
plt.xlabel('LM_WT values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Production
plt.figure(figsize=(10, 6))
plt.hist(data['Production'], bins=20)
plt.title('Histogram of Production')
plt.xlabel('Production values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()



#=======================================================================================================================
#scatter plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

steel1 = pd.read_csv(r"C:/Users/shrad/Desktop/360 PDA/PROJECT/SQL DOC/steel1.csv")
print(steel1)

steel1.columns=steel1.columns.str.strip()
steel1.info()

#plt.scatter(x = steel1['TP'], y = steel1['TP']) 

#plt.scatter(x = steel1['HP'], y = steel1['SP'], color = 'green') 

sns.pairplot(steel1,vars=['INJ1_QTY','INJ2_QTY','DRI1_QTY','DRI2_QTY','TOT_DRI_QTY','HOT_METAL'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['BSM','TP','MSTB','SKULL','SHRAD','REMET','BP','HBI','OTHERS','SCRAP_QTY','PIGIRON'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['Hot_Heel','Hot_Heel','DOLO1_EMPTY','TOT_LIME_QTY','O2ACT','ENERGY','KWH_PER_TON'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['MELT_TIME','TA_TIME','TT_TIME','TA_TIME','TT_TIME','Production'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['E1_CUR','E2_CUR','E3_CUR','SPOUT','C','LM_WT'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['SI','MN','P','S','CU','CR'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['NI','N','OPEN_C','TAP_C','IT_KG','STATIC_WT'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['LIME','O2SIDE1','O2SIDE2','O2SIDE3','PREV_TAP_TIME','Pour_Back_Metal'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['TAP_TEMP','TO2REQ','KWH_PER_MIN','ARCING_TIME','DOWN_TIME','DOLOMIT','CPC'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['TEMPERATURE','POWER','TIME_UTLN_PRCNT','BUCKET_NO','LIME2'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['SPINNING','RAMMING1','RAMMING2','TAP_DURATION'] , palette='coolwarm')
plt.show()

sns.pairplot(steel1,vars=['POW_ON_TIME','TAPPING_TIME','LAB_REP_TIME','PREV_TAP_TIME'] , palette='coolwarm')
plt.show()

#HEAT MAP

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:/Users/shrad/Desktop/360 PDA/PROJECT/SQL DOC/steel1.csv")
print(data)
data.info()

selected_features = ['INJ2_QTY','TP','BSM','MSTB','SKULL','SHRAD','REMET','BP','HBI','OTHERS','PIGIRON','DRI2_QTY','TOT_DRI_QTY','Total Charge','DOLO', 'TOT_LIME_QTY', 'O2ACT']
sns.heatmap(data[selected_features].corr(), annot=True, cmap='coolwarm')
plt.show()


selected_features = ['C', 'SI', 'MN', 'P', 'S', 'CU', 'CR', 'TAP_C', 'IT_KG', 'BUCKET_NO','STATIC_WT', 'LIME', 'LIME2', 'O2SIDE1']
sns.heatmap(data[selected_features].corr(), annot=True, cmap='coolwarm')
plt.show()

selected_features = ['O2SIDE2', 'O2SIDE3','SPINNING','RAMMING1', 'RAMMING2', 'TAP_DURATION', 'Pour_Back_Metal', 'LM_WT']
sns.heatmap(data[selected_features].corr(), annot=True, cmap='coolwarm')
plt.show()


# CORELATION COEFICIENT

# Importing the pandas library for data manipulation and analysis
import pandas as pd  

# Reading data from a CSV file named "steeel.csv" located at "C:/Users/Admin/Desktop/C0DE/"
data = pd.read_csv(r"C:/Users/shrad/Desktop/360 PDA/PROJECT/SQL DOC/steel1.csv")

# Removing non-numeric columns (e.g., date columns) for correlation calculation
numeric_data = data.select_dtypes(include='number')

# Calculating the correlation matrix for the numeric columns in the DataFrame
correlation_matrix = numeric_data.corr()

# Print the correlation matrix
print(correlation_matrix)


import numpy as np
import matplotlib.pyplot as plt

# Example data for 'INJ1_QTY' column (replace with your actual data)
data_INJ1_QTY = np.random.randint(1, 100, size=773)

# Create bar plot for 'INJ1_QTY'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_INJ1_QTY)), data_INJ1_QTY, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('INJ1_QTY Values')
plt.title('Bar Plot: INJ1_QTY')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'INJ2_QTY' column (replace with your actual data)
data_INJ2_QTY = np.random.randint(1, 100, size=773)

# Create bar plot for 'INJ2_QTY'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_INJ2_QTY)), data_INJ2_QTY, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('INJ2_QTY Values')
plt.title('Bar Plot: INJ2_QTY')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'BSM' column (replace with your actual data)
data_BSM = np.random.randint(1, 100, size=773)

# Create bar plot for 'BSM'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_BSM)), data_BSM, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('BSM Values')
plt.title('Bar Plot: BSM')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'TP' column (replace with your actual data)
data_TP = np.random.randint(1, 100, size=773)

# Create bar plot for 'TP'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TP)), data_TP, color='orange', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TP Values')
plt.title('Bar Plot: TP')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'MSTB' column (replace with your actual data)
data_MSTB = np.random.randint(1, 100, size=773)

# Create bar plot for 'MSTB'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_MSTB)), data_MSTB, color='purple', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('MSTB Values')
plt.title('Bar Plot: MSTB')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'SKULL' column (replace with your actual data)
data_SKULL = np.random.randint(1, 100, size=773)

# Create bar plot for 'SKULL'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_SKULL)), data_SKULL, color='brown', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('SKULL Values')
plt.title('Bar Plot: SKULL')
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Example data for 'SHRAD' column (replace with your actual data)
data_SHRAD = np.random.randint(1, 100, size=773)

# Create bar plot for 'SHRAD'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_SHRAD)), data_SHRAD, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('SHRAD Values')
plt.title('Bar Plot: SHRAD')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'REMET' column (replace with your actual data)
data_REMET = np.random.randint(1, 100, size=773)

# Create bar plot for 'REMET'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_REMET)), data_REMET, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('REMET Values')
plt.title('Bar Plot: REMET')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'BP' column (replace with your actual data)
data_BP = np.random.randint(1, 100, size=773)

# Create bar plot for 'BP'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_BP)), data_BP, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('BP Values')
plt.title('Bar Plot: BP')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'HBI' column (replace with your actual data)
data_HBI = np.random.randint(1, 100, size=773)

# Create bar plot for 'HBI'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_HBI)), data_HBI, color='orange', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('HBI Values')
plt.title('Bar Plot: HBI')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'OTHERS' column (replace with your actual data)
data_OTHERS = np.random.randint(1, 100, size=773)

# Create bar plot for 'OTHERS'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_OTHERS)), data_OTHERS, color='purple', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('OTHERS Values')
plt.title('Bar Plot: OTHERS')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'SCRAP_QTY' column (replace with your actual data)
data_SCRAP_QTY = np.random.randint(1, 100, size=773)

# Create bar plot for 'SCRAP_QTY'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_SCRAP_QTY)), data_SCRAP_QTY, color='brown', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('SCRAP_QTY Values')
plt.title('Bar Plot: SCRAP_QTY')
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Example data for 'PIGIRON' column (replace with your actual data)
data_PIGIRON = np.random.randint(1, 100, size=773)

# Create bar plot for 'PIGIRON'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_PIGIRON)), data_PIGIRON, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('PIGIRON Values')
plt.title('Bar Plot: PIGIRON')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'DRI1_QTY' column (replace with your actual data)
data_DRI1_QTY = np.random.randint(1, 100, size=773)

# Create bar plot for 'DRI1_QTY'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_DRI1_QTY)), data_DRI1_QTY, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('DRI1_QTY Values')
plt.title('Bar Plot: DRI1_QTY')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'DRI2_QTY' column (replace with your actual data)
data_DRI2_QTY = np.random.randint(1, 100, size=773)

# Create bar plot for 'DRI2_QTY'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_DRI2_QTY)), data_DRI2_QTY, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('DRI2_QTY Values')
plt.title('Bar Plot: DRI2_QTY')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'TOT_DRI_QTY' column (replace with your actual data)
data_TOT_DRI_QTY = np.random.randint(1, 100, size=773)

# Create bar plot for 'TOT_DRI_QTY'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TOT_DRI_QTY)), data_TOT_DRI_QTY, color='orange', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TOT_DRI_QTY Values')
plt.title('Bar Plot: TOT_DRI_QTY')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'HOT_METAL' column (replace with your actual data)
data_HOT_METAL = np.random.randint(1, 100, size=773)

# Create bar plot for 'HOT_METAL'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_HOT_METAL)), data_HOT_METAL, color='purple', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('HOT_METAL Values')
plt.title('Bar Plot: HOT_METAL')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'TotalCharge' column (replace with your actual data)
data_TotalCharge = np.random.randint(1, 100, size=773)

# Create bar plot for 'TotalCharge'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TotalCharge)), data_TotalCharge, color='brown', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TotalCharge Values')
plt.title('Bar Plot: TotalCharge')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'Hot_Heel' column (replace with your actual data)
data_Hot_Heel = np.random.randint(1, 100, size=773)

# Create bar plot for 'Hot_Heel'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_Hot_Heel)), data_Hot_Heel, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('Hot_Heel Values')
plt.title('Bar Plot: Hot_Heel')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'DOLO' column (replace with your actual data)
data_DOLO = np.random.randint(1, 100, size=773)

# Create bar plot for 'DOLO'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_DOLO)), data_DOLO, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('DOLO Values')
plt.title('Bar Plot: DOLO')
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Example data for 'DOLO1_EMPTY' column (replace with your actual data)
data_DOLO1_EMPTY = np.random.randint(1, 100, size=773)

# Create bar plot for 'DOLO1_EMPTY'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_DOLO1_EMPTY)), data_DOLO1_EMPTY, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('DOLO1_EMPTY Values')
plt.title('Bar Plot: DOLO1_EMPTY')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'TOT_LIME_QTY' column (replace with your actual data)
data_TOT_LIME_QTY = np.random.randint(1, 100, size=773)

# Create bar plot for 'TOT_LIME_QTY'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TOT_LIME_QTY)), data_TOT_LIME_QTY, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TOT_LIME_QTY Values')
plt.title('Bar Plot: TOT_LIME_QTY')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'TAP_TEMP' column (replace with your actual data)
data_TAP_TEMP = np.random.randint(1, 100, size=773)

# Create bar plot for 'TAP_TEMP'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TAP_TEMP)), data_TAP_TEMP, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TAP_TEMP Values')
plt.title('Bar Plot: TAP_TEMP')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'O2REQ' column (replace with your actual data)
data_O2REQ = np.random.randint(1, 100, size=773)

# Create bar plot for 'O2REQ'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_O2REQ)), data_O2REQ, color='orange', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('O2REQ Values')
plt.title('Bar Plot: O2REQ')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'O2ACT' column (replace with your actual data)
data_O2ACT = np.random.randint(1, 100, size=773)

# Create bar plot for 'O2ACT'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_O2ACT)), data_O2ACT, color='purple', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('O2ACT Values')
plt.title('Bar Plot: O2ACT')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'ENERGY' column (replace with your actual data)
data_ENERGY = np.random.randint(1, 100, size=773)

# Create bar plot for 'ENERGY'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_ENERGY)), data_ENERGY, color='brown', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('ENERGY Values')
plt.title('Bar Plot: ENERGY')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'KWH_PER_TON' column (replace with your actual data)
data_KWH_PER_TON = np.random.randint(1, 100, size=773)

# Create bar plot for 'KWH_PER_TON'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_KWH_PER_TON)), data_KWH_PER_TON, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('KWH_PER_TON Values')
plt.title('Bar Plot: KWH_PER_TON')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'KWH_PER_MIN' column (replace with your actual data)
data_KWH_PER_MIN = np.random.randint(1, 100, size=773)

# Create bar plot for 'KWH_PER_MIN'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_KWH_PER_MIN)), data_KWH_PER_MIN, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('KWH_PER_MIN Values')
plt.title('Bar Plot: KWH_PER_MIN')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'MELT_TIME' column (replace with your actual data)
data_MELT_TIME = np.random.randint(1, 100, size=773)

# Create bar plot for 'MELT_TIME'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_MELT_TIME)), data_MELT_TIME, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('MELT_TIME Values')
plt.title('Bar Plot: MELT_TIME')
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Example data for 'TA_TIME' column (replace with your actual data)
data_TA_TIME = np.random.randint(1, 100, size=773)

# Create bar plot for 'TA_TIME'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TA_TIME)), data_TA_TIME, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TA_TIME Values')
plt.title('Bar Plot: TA_TIME')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'TT_TIME' column (replace with your actual data)
data_TT_TIME = np.random.randint(1, 100, size=773)

# Create bar plot for 'TT_TIME'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TT_TIME)), data_TT_TIME, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TT_TIME Values')
plt.title('Bar Plot: TT_TIME')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'ARCING_TIME' column (replace with your actual data)
data_ARCING_TIME = np.random.randint(1, 100, size=773)

# Create bar plot for 'ARCING_TIME'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_ARCING_TIME)), data_ARCING_TIME, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('ARCING_TIME Values')
plt.title('Bar Plot: ARCLING_TIME')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'DOWN_TIME' column (replace with your actual data)
data_DOWN_TIME = np.random.randint(1, 100, size=773)

# Create bar plot for 'DOWN_TIME'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_DOWN_TIME)), data_DOWN_TIME, color='orange', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('DOWN_TIME Values')
plt.title('Bar Plot: DOWN_TIME')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'E1_CUR' column (replace with your actual data)
data_E1_CUR = np.random.randint(1, 100, size=773)

# Create bar plot for 'E1_CUR'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_E1_CUR)), data_E1_CUR, color='purple', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('E1_CUR Values')
plt.title('Bar Plot: E1_CUR')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'E2_CUR' column (replace with your actual data)
data_E2_CUR = np.random.randint(1, 100, size=773)

# Create bar plot for 'E2_CUR'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_E2_CUR)), data_E2_CUR, color='brown', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('E2_CUR Values')
plt.title('Bar Plot: E2_CUR')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'E3_CUR' column (replace with your actual data)
data_E3_CUR = np.random.randint(1, 100, size=773)

# Create bar plot for 'E3_CUR'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_E3_CUR)), data_E3_CUR, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('E3_CUR Values')
plt.title('Bar Plot: E3_CUR')
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Example data for 'SPOUT' column (replace with your actual data)
data_SPOUT = np.random.randint(1, 100, size=773)

# Create bar plot for 'SPOUT'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_SPOUT)), data_SPOUT, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('SPOUT Values')
plt.title('Bar Plot: SPOUT')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'DOLOMIT' column (replace with your actual data)
data_DOLOMIT = np.random.randint(1, 100, size=773)

# Create bar plot for 'DOLOMIT'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_DOLOMIT)), data_DOLOMIT, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('DOLOMIT Values')
plt.title('Bar Plot: DOLOMIT')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'CPC' column (replace with your actual data)
data_CPC = np.random.randint(1, 100, size=773)

# Create bar plot for 'CPC'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_CPC)), data_CPC, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('CPC Values')
plt.title('Bar Plot: CPC')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'TEMPERATURE' column (replace with your actual data)
data_TEMPERATURE = np.random.randint(1, 100, size=773)

# Create bar plot for 'TEMPERATURE'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TEMPERATURE)), data_TEMPERATURE, color='orange', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TEMPERATURE Values')
plt.title('Bar Plot: TEMPERATURE')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'POWER' column (replace with your actual data)
data_POWER = np.random.randint(1, 100, size=773)

# Create bar plot for 'POWER'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_POWER)), data_POWER, color='purple', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('POWER Values')
plt.title('Bar Plot: POWER')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'C' column (replace with your actual data)
data_C = np.random.randint(1, 100, size=773)

# Create bar plot for 'C'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_C)), data_C, color='brown', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('C Values')
plt.title('Bar Plot: C')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'SI' column (replace with your actual data)
data_SI = np.random.randint(1, 100, size=773)

# Create bar plot for 'SI'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_SI)), data_SI, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('SI Values')
plt.title('Bar Plot: SI')
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Example data for 'MN' column (replace with your actual data)
data_MN = np.random.randint(1, 100, size=773)

# Create bar plot for 'MN'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_MN)), data_MN, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('MN Values')
plt.title('Bar Plot: MN')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'P' column (replace with your actual data)
data_P = np.random.randint(1, 100, size=773)

# Create bar plot for 'P'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_P)), data_P, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('P Values')
plt.title('Bar Plot: P')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'S' column (replace with your actual data)
data_S = np.random.randint(1, 100, size=773)

# Create bar plot for 'S'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_S)), data_S, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('S Values')
plt.title('Bar Plot: S')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'CU' column (replace with your actual data)
data_CU = np.random.randint(1, 100, size=773)

# Create bar plot for 'CU'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_CU)), data_CU, color='orange', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('CU Values')
plt.title('Bar Plot: CU')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'CR' column (replace with your actual data)
data_CR = np.random.randint(1, 100, size=773)

# Create bar plot for 'CR'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_CR)), data_CR, color='purple', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('CR Values')
plt.title('Bar Plot: CR')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'NI' column (replace with your actual data)
data_NI = np.random.randint(1, 100, size=773)

# Create bar plot for 'NI'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_NI)), data_NI, color='brown', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('NI Values')
plt.title('Bar Plot: NI')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'N' column (replace with your actual data)
data_N = np.random.randint(1, 100, size=773)

# Create bar plot for 'N'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_N)), data_N, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('N Values')
plt.title('Bar Plot: N')
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Example data for 'TIME_UTLN_PRCNT' column (replace with your actual data)
data_TIME_UTLN_PRCNT = np.random.randint(1, 100, size=773)

# Create bar plot for 'TIME_UTLN_PRCNT'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TIME_UTLN_PRCNT)), data_TIME_UTLN_PRCNT, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TIME_UTLN_PRCNT Values')
plt.title('Bar Plot: TIME_UTLN_PRCNT')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'TOP_COKE' column (replace with your actual data)
data_TOP_COKE = np.random.randint(1, 100, size=773)

# Create bar plot for 'TOP_COKE'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TOP_COKE)), data_TOP_COKE, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TOP_COKE Values')
plt.title('Bar Plot: TOP_COKE')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'OPEN_C' column (replace with your actual data)
data_OPEN_C = np.random.randint(1, 100, size=773)

# Create bar plot for 'OPEN_C'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_OPEN_C)), data_OPEN_C, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('OPEN_C Values')
plt.title('Bar Plot: OPEN_C')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'TAP_C' column (replace with your actual data)
data_TAP_C = np.random.randint(1, 100, size=773)

# Create bar plot for 'TAP_C'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TAP_C)), data_TAP_C, color='orange', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TAP_C Values')
plt.title('Bar Plot: TAP_C')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'IT_KG' column (replace with your actual data)
data_IT_KG = np.random.randint(1, 100, size=773)

# Create bar plot for 'IT_KG'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_IT_KG)), data_IT_KG, color='purple', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('IT_KG Values')
plt.title('Bar Plot: IT_KG')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'BUCKET_NO' column (replace with your actual data)
data_BUCKET_NO = np.random.randint(1, 100, size=773)

# Create bar plot for 'BUCKET_NO'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_BUCKET_NO)), data_BUCKET_NO, color='brown', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('BUCKET_NO Values')
plt.title('Bar Plot: BUCKET_NO')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'STATIC_WT' column (replace with your actual data)
data_STATIC_WT = np.random.randint(1, 100, size=773)

# Create bar plot for 'STATIC_WT'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_STATIC_WT)), data_STATIC_WT, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('STATIC_WT Values')
plt.title('Bar Plot: STATIC_WT')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'LIME' column (replace with your actual data)
data_LIME = np.random.randint(1, 100, size=773)

# Create bar plot for 'LIME'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_LIME)), data_LIME, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('LIME Values')
plt.title('Bar Plot: LIME')
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Example data for 'LIME2' column (replace with your actual data)
data_LIME2 = np.random.randint(1, 100, size=773)

# Create bar plot for 'LIME2'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_LIME2)), data_LIME2, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('LIME2 Values')
plt.title('Bar Plot: LIME2')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'O2SIDE1' column (replace with your actual data)
data_O2SIDE1 = np.random.randint(1, 100, size=773)

# Create bar plot for 'O2SIDE1'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_O2SIDE1)), data_O2SIDE1, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('O2SIDE1 Values')
plt.title('Bar Plot: O2SIDE1')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'O2SIDE2' column (replace with your actual data)
data_O2SIDE2 = np.random.randint(1, 100, size=773)

# Create bar plot for 'O2SIDE2'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_O2SIDE2)), data_O2SIDE2, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('O2SIDE2 Values')
plt.title('Bar Plot: O2SIDE2')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'O2SIDE3' column (replace with your actual data)
data_O2SIDE3 = np.random.randint(1, 100, size=773)

# Create bar plot for 'O2SIDE3'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_O2SIDE3)), data_O2SIDE3, color='orange', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('O2SIDE3 Values')
plt.title('Bar Plot: O2SIDE3')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'SPINNING' column (replace with your actual data)
data_SPINNING = np.random.randint(1, 100, size=773)

# Create bar plot for 'SPINNING'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_SPINNING)), data_SPINNING, color='purple', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('SPINNING Values')
plt.title('Bar Plot: SPINNING')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'RAMMING1' column (replace with your actual data)
data_RAMMING1 = np.random.randint(1, 100, size=773)

# Create bar plot for 'RAMMING1'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_RAMMING1)), data_RAMMING1, color='brown', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('RAMMING1 Values')
plt.title('Bar Plot: RAMMING1')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'RAMMING2' column (replace with your actual data)
data_RAMMING2 = np.random.randint(1, 100, size=773)

# Create bar plot for 'RAMMING2'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_RAMMING2)), data_RAMMING2, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('RAMMING2 Values')
plt.title('Bar Plot: RAMMING2')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'TAP_DURATION' column (replace with your actual data)
data_TAP_DURATION = np.random.randint(1, 100, size=773)

# Create bar plot for 'TAP_DURATION'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_TAP_DURATION)), data_TAP_DURATION, color='green', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('TAP_DURATION Values')
plt.title('Bar Plot: TAP_DURATION')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'Pour_Back_Metal' column (replace with your actual data)
data_Pour_Back_Metal = np.random.randint(1, 100, size=773)

# Create bar plot for 'Pour_Back_Metal'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_Pour_Back_Metal)), data_Pour_Back_Metal, color='red', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('Pour_Back_Metal Values')
plt.title('Bar Plot: Pour_Back_Metal')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'LM_WT' column (replace with your actual data)
data_LM_WT = np.random.randint(1, 100, size=773)

# Create bar plot for 'LM_WT'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_LM_WT)), data_LM_WT, color='orange', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('LM_WT Values')
plt.title('Bar Plot: LM_WT')
plt.grid(True)
plt.tight_layout()
plt.show()

# Example data for 'Production' column (replace with your actual data)
data_Production = np.random.randint(1, 100, size=773)

# Create bar plot for 'Production'
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(data_Production)), data_Production, color='purple', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('Production Values')
plt.title('Bar Plot: Production')
plt.grid(True)
plt.tight_layout()
plt.show()

# LINE CHART
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:/Users/shrad/Desktop/360 PDA/PROJECT/SQL DOC/steel1.csv")
df = df.sort_values(by='DATETIME')
df.columns=data.columns.str.strip()
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['INJ1_QTY'])
plt.xlabel('dateandtime')
plt.ylabel('Qty in of date and time')
plt.title('Time Plot')
plt.grid(True)
plt.show()



# Plot for INJ2_QTY
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['INJ2_QTY'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for INJ2_QTY')
plt.grid(True)
plt.show()

# Plot for BSM
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['BSM'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for BSM')
plt.grid(True)
plt.show()

# Plot for BP
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['BP'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for BP')
plt.grid(True)
plt.show()

# Plot for HBI
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['HBI'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for HBI')
plt.grid(True)
plt.show()

# Plot for OTHERS
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['OTHERS'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for OTHERS')
plt.grid(True)
plt.show()

# Plot for SCRAP_QTY
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['SCRAP_QTY'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for SCRAP_QTY')
plt.grid(True)
plt.show()

# Plot for PIGIRON
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['PIGIRON'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for PIGIRON')
plt.grid(True)
plt.show()

# Plot for DRI1_QTY
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['DRI1_QTY'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for DRI1_QTY')
plt.grid(True)
plt.show()

# Plot for DRI2_QTY
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['DRI2_QTY'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for DRI2_QTY')
plt.grid(True)
plt.show()

# Plot for TOT_DRI_QTY
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['TOT_DRI_QTY'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for TOT_DRI_QTY')
plt.grid(True)
plt.show()

# Plot for HOT_METAL
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['HOT_METAL'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for HOT_METAL')
plt.grid(True)
plt.show()

# Plot for TotalCharge
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['TotalCharge'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for TotalCharge')
plt.grid(True)
plt.show()

# Plot for Hot_Heel
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['Hot_Heel'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for Hot_Heel')
plt.grid(True)
plt.show()

# Plot for DOLO
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['DOLO'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for DOLO')
plt.grid(True)
plt.show()

# Plot for DOLO1_EMPTY
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['DOLO1_EMPTY'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for DOLO1_EMPTY')
plt.grid(True)
plt.show()

# Plot for TOT_LIME_QTY
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['TOT_LIME_QTY'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for TOT_LIME_QTY')
plt.grid(True)
plt.show()

# Plot for TAP_TEMP
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['TAP_TEMP'])
plt.xlabel('Date and Time')
plt.ylabel('Temperature')
plt.title('Time Plot for TAP_TEMP')
plt.grid(True)
plt.show()

# Plot for O2ACT
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['O2ACT'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for O2ACT')
plt.grid(True)
plt.show()

# Plot for ENERGY
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['ENERGY'])
plt.xlabel('Date and Time')
plt.ylabel('Energy')
plt.title('Time Plot for ENERGY')
plt.grid(True)
plt.show()

# Plot for KWH_PER_TON
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['KWH_PER_TON'])
plt.xlabel('Date and Time')
plt.ylabel('KWH/Ton')
plt.title('Time Plot for KWH_PER_TON')
plt.grid(True)
plt.show()

# Plot for KWH_PER_MIN
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['KWH_PER_MIN'])
plt.xlabel('Date and Time')
plt.ylabel('KWH/Min')
plt.title('Time Plot for KWH_PER_MIN')
plt.grid(True)
plt.show()

# Plot for MELT_TIME
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['MELT_TIME'])
plt.xlabel('Date and Time')
plt.ylabel('Time')
plt.title('Time Plot for MELT_TIME')
plt.grid(True)
plt.show()

# Plot for TA_TIME
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['TA_TIME'])
plt.xlabel('Date and Time')
plt.ylabel('Time')
plt.title('Time Plot for TA_TIME')
plt.grid(True)
plt.show()

# Plot for TT_TIME
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['TT_TIME'])
plt.xlabel('Date and Time')
plt.ylabel('Time')
plt.title('Time Plot for TT_TIME')
plt.grid(True)
plt.show()

# Plot for E1_CUR
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['E1_CUR'])
plt.xlabel('Date and Time')
plt.ylabel('Current')
plt.title('Time Plot for E1_CUR')
plt.grid(True)
plt.show()

# Plot for E2_CUR
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['E2_CUR'])
plt.xlabel('Date and Time')
plt.ylabel('Current')
plt.title('Time Plot for E2_CUR')
plt.grid(True)
plt.show()

# Plot for E3_CUR
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['E3_CUR'])
plt.xlabel('Date and Time')
plt.ylabel('Current')
plt.title('Time Plot for E3_CUR')
plt.grid(True)
plt.show()

# Plot for SPOUT
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['SPOUT'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for SPOUT')
plt.grid(True)
plt.show()

# Plot for C
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['C'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for C')
plt.grid(True)
plt.show()

# Plot for SI
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['SI'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for SI')
plt.grid(True)
plt.show()

# Plot for MN
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['MN'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for MN')
plt.grid(True)
plt.show()

# Plot for P
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['P'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for P')
plt.grid(True)
plt.show()

# Plot for S
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['S'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for S')
plt.grid(True)
plt.show()

# Plot for CU
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['CU'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for CU')
plt.grid(True)
plt.show()

# Plot for CR
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['CR'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for CR')
plt.grid(True)
plt.show()

# Plot for TAP_C
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['TAP_C'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for TAP_C')
plt.grid(True)
plt.show()

# Plot for IT_KG
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['IT_KG'])
plt.xlabel('Date and Time')
plt.ylabel('Weight')
plt.title('Time Plot for IT_KG')
plt.grid(True)
plt.show()

# Plot for BUCKET_NO
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['BUCKET_NO'])
plt.xlabel('Date and Time')
plt.ylabel('Number')
plt.title('Time Plot for BUCKET_NO')
plt.grid(True)
plt.show()

# Plot for STATIC_WT
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['STATIC_WT'])
plt.xlabel('Date and Time')
plt.ylabel('Weight')
plt.title('Time Plot for STATIC_WT')
plt.grid(True)
plt.show()

# Plot for LIME
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['LIME'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for LIME')
plt.grid(True)
plt.show()

# Plot for LIME2
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['LIME2'])
plt.xlabel('Date and Time')
plt.ylabel('Quantity')
plt.title('Time Plot for LIME2')
plt.grid(True)
plt.show()

# Plot for O2SIDE1
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['O2SIDE1'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for O2SIDE1')
plt.grid(True)
plt.show()

# Plot for O2SIDE2
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['O2SIDE2'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for O2SIDE2')
plt.grid(True)
plt.show()

# Plot for O2SIDE3
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['O2SIDE3'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for O2SIDE3')
plt.grid(True)
plt.show()

# Plot for SPINNING
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['SPINNING'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for SPINNING')
plt.grid(True)
plt.show()

# Plot for RAMMING1
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['RAMMING1'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for RAMMING1')
plt.grid(True)
plt.show()

# Plot for RAMMING2
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['RAMMING2'])
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.title('Time Plot for RAMMING2')
plt.grid(True)
plt.show()

# Plot for TAP_DURATION
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['TAP_DURATION'])
plt.xlabel('Date and Time')
plt.ylabel('Duration')
plt.title('Time Plot for TAP_DURATION')
plt.grid(True)
plt.show()

# Plot for Pour_Back_Metal
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['Pour_Back_Metal'])
plt.xlabel('Date and Time')
plt.ylabel('Metal')
plt.title('Time Plot for Pour_Back_Metal')
plt.grid(True)
plt.show()

# Plot for LM_WT
plt.figure(figsize=(10, 6))
plt.plot(df['DATETIME'], df['LM_WT'])
plt.xlabel('Date and Time')
plt.ylabel('Weight')
plt.title('Time Plot for LM_WT')
plt.grid(True)
plt.show()
