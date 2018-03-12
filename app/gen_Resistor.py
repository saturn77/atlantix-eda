#====================================
#
#  Title   : Programmatically Generated Libraries 
#  File    : gen_Resistor.py
#  Author  : Atlantix Engineering
#  Descrip : Generate a resistor library for Altium Designer 
#  
#  LICENSE : MIT
# 
#====================================
import re
import sys
from time import strftime
#==========================================================
# GUI CONSTRUCT NEEDED HERE FOR "BROWSE TO FILE TO SAVE"
fname = "C:\\Users\\james\\repos\\atlantix\\atlantix_toolset\\atlantix_altiumLib\\Atlantix_R.csv"

# ========================================================
sys.stdout = open(fname,'w')
#f = open(fname,'w')
print("Part,Description,Value,Case,Tol,Power,Manufacturer,Manufacturer P/N,Supplier 1,Supplier Part Number 1,Library Path,Library Ref,Footprint Path,Footprint Ref,Company")
    #-------------------------------------
    # Generate 0603 Values, E96, 1%
    #-------------------------------------

series = 96; 
Sizes   = ["0402", "0603", "0805"]; 

def compRvalues(series):
    z = float(series)
    return [round(10.0**(float(y/z)),2) for y in range(int(z))]


Rvalues = compRvalues(series)

Decades = [1, 10, 100, 1000, 10000, 100000, 1000000]
Rstring = ""
Digikey  = ""

tol = "100ppm"
for size in Sizes: 
    for decade in Decades:
        for value in Rvalues:
            res = decade * value
            Z = str(value)
            if decade == 1:         
                Rstring = '{:1.2f}'.format(res) 
                #Digikey  =  Z[0:1] + 'R' + Z[2] + 'F'  
                Digikey = re.sub(r"(\.)", "R", Rstring)
            elif decade == 10: 
                Rstring = "%.1f" %res
                #Digikey  =  Z[0:1] + 'R' + Z[2] + 'F'  
                Digikey = re.sub(r"(\.)", "R", Rstring)
            elif decade == 100: 
                Rstring = '{:3.0f}'.format(res) 
                Digikey  =  Rstring + 'R'
            elif decade == 1000:
                alpha   = res/1000 
                Rstring = '{:1.2f}'.format(alpha) + 'K' 
                #Digikey  =  Z[0:3] + '1' + 'F'
                Digikey = re.sub(r"(\.)", "K", Rstring)
                Digikey = Digikey[:-1]
            elif decade == 10000:
                alpha   = res/1000
                Rstring = '{:2.1f}'.format(alpha) + 'K'
                #Digikey  =  Z[0:3] + '2' + 'F'
                Digikey = re.sub(r"(\.)", "K", Rstring)
                Digikey = Digikey[:-1]
            elif decade == 100000:
                alpha  = res/1000
                #Rstring = res 
                Rstring = '{:3.0f}'.format(alpha) + 'K'
                #Digikey  =  Z[0:3] + '3' + 'F'
                Digikey = re.sub(r"(\.)", "K", Rstring)
            else:
                break  

            if size == "0402":
                if decade == 1:
                    digikey = "541-%sLLCT-ND" %Rstring 
                else:
                    digikey = "541-%sLCT-ND" %Rstring 
                vishay = "CRCW%s%sFKED" %(size,Digikey)
                power  = "62mW"
            elif size == "0603":
                if decade == 1:
                    digikey = "541-%sHHCT-ND" %Rstring
                else:
                    digikey =  "541-%sHCT-ND" %Rstring
                vishay = "CRCW%s%sFKEA" %(size,Digikey)
                power  = "100mW"
            elif size == "0805":
                if decade == 1:
                    digikey = "541-%sCCCT-ND" %Rstring
                else:
                    digikey = "541-%sCCT-ND" %Rstring 
                vishay = "CRCW%s%sFKEA" %(size,Digikey)
                power  = "125mW"
            else:
                break
            print("RES_%s_%s,RES SMT %s %s %s %s,%s,%s,%s,%s,Vishay-Dale,%s,Digi-key,%s,Atlantix_R.SchLib,Res1,Atlantix_R.PcbLib,RES%s,Atlantix_Engineering" \
            %(size,Rstring,Rstring,size,tol,power,Rstring,size,tol,power,vishay,digikey,size))   


#print("Summary")
#print("Resistor library generation complete")
#print("The library pathname is :\n" + fname + "\nLibrary was created on:\n " + strftime("%m/%d/%Y at %H.%M hours"))


