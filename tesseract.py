import os
import re
import csv

def findFunc():

    pathList = []

    #stores file names from master folder in a list
    i = 1
    for filename in os.listdir(r'C:\Users\mclark\Desktop\python\flask'):
        if filename.endswith('image' + str(i) + '.png'):
            i = i+1
            pathList.append(os.path.join(r'C:\Users\mclark\Desktop\python\flask', filename))
            continue
        else:
            continue
    #if len(pathList) >= 10:
        #myorder = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        #pathList = [pathList[l] for l in myorder]
    #print(list)

    #This script is used to call tesseract from the command prompt
    try:
        from PIL import Image
    except ImportError:
        import Image
    import pytesseract

    def ocr_core(coverpage):
        """
        This function will handle the core OCR processing of images.
        """
    # uses Pillow's Image class to open the image and pytesseract to detect the string in the image
        text = pytesseract.image_to_string(Image.open(coverpage), \
            config='--psm 6')
        return text

    listoflists = []

    #iterates over file names and has tesseract print output
    for path in pathList:
        splitpath = re.split(':|\n',ocr_core(path))
        #splitpath2 = [x.replace('\n', ' ') for x in splitpath]
        splitpath2 = list(filter(None, splitpath))
        listoflists.append(splitpath2)
        #listoflists.append(splitpath2)
        #target and grab specific information HERE
    #print(listoflists)
    #This gets the title
    indices = [i for i, s in enumerate(listoflists[0]) if 'ANALYSIS' in s]
    print((listoflists[0][(indices[0] + 1)]))
    #print(listoflists[0][5])
    #This gets address
    print((listoflists[0][(indices[0] + 2)])+' '+(listoflists[0][(indices[0] + 3)]))
    #This gets Parcel Number
    parcelHead = listoflists[0].index('Parcel Number')
    parcelNumVar = (listoflists[0][(parcelHead + 1)])
    print(parcelNumVar)
    #This gets Petition Number
    petitionHead = listoflists[0].index('Petition Number')
    petitionNumVar = (listoflists[0][(petitionHead + 1)])
    print(petitionNumVar)
    #print(listoflists[0][11])
    #This gets Roll Year
    indices2 = [i for i, s in enumerate(listoflists[0]) if 'Valorem' in s]
    rollYearVar = (listoflists[0][indices2[0]])[:-27]
    print(rollYearVar)
    #print((listoflists[0][26])[:-27])
    #print((listoflists[0][16])[:-27])) w/o psm 6

    #print(listoflists[1])
    #This gets Improvement Data
    imprData = ''
    try:
        imprHead = listoflists[1].index('Improvement Data')
        imprTail = listoflists[1].index('Zoning')
        while imprHead != (imprTail -1):
            imprHead += 1
            imprData = imprData + listoflists[1][imprHead] + ' '
        imprDataVar = imprData[1:]
        print(imprDataVar)
    except:
        imprDataVar = "Improvement Data not found"
        print(imprDataVar)
        pass
    #print((listoflists[1][23])+' '+(listoflists[1][24])) w/o psm 6
    #This gets Zoning
    try:
        zoningVar = (listoflists[1][(imprTail +1)])[1:]
        print(zoningVar)
    except:
        zoningVar = "Zoning not found"
        print(zoningVar)
        pass
    #This gets Tangible Personal Property
    try:
        tangHead = listoflists[1].index('Tangible Personal Property')
        tangVar = (listoflists[1][(tangHead + 1)])[1:]
        print(tangVar)
    except:
        tangVar = "Tangible Personal Property not found"
        print(tangVar)
        pass
    #print(listoflists[1][28])
    #This gets Cost Approach Value
    try:
        costHead = listoflists[1].index('Cost Approach')
        costApp = (listoflists[1][(costHead + 1)]).replace('$','')
        costApp2 = costApp.replace(',','')
        costVar = costApp2[1:]
        print(costVar)
    except:
        costVar = "Cost Approach Value not found"
        print(costVar)
        pass
    #This gets Sales Approach Min
    try:
        salesHead = listoflists[1].index('Sales Approach')
        salesApp = (listoflists[1][(salesHead +1)]).replace('$','')
        salesApp2 = salesApp.replace(',','')
        salesApp3 = salesApp2.split('-')
        salesMinVar = (salesApp3[0])[1:]
        print(salesMinVar)
    except:
        salesMinVar = "Sales Approach Min not found"
        print(salesMinVar)
    #This gets Sales Approach Max
    try:
        salesMaxVar = (salesApp3[1])[1:]
        print(salesMaxVar)
    except:
        salesMaxVar = "Sales Approach Max not found"
        print(salesMaxVar)
        pass
    #This gets Income Approach
    try:
        incomeHead = listoflists[1].index('Income Approach')
        incomeApp = (listoflists[1][(incomeHead + 1)]).replace('$','')
        incomeApp2 = incomeApp.replace(',','')
        incomeApp3 = incomeApp2[1:]
        print(incomeApp3)
    except:
        incomeApp3 = "Income Approach not found"
        print(incomeApp3)
        pass
    #incomeApp = (listoflists[1][31]).replace('$','')
    #incomeApp2 = incomeApp.replace(',','')
    #print(incomeApp2)

    #print(listoflists[4])
    #This gets Occupancy
    try:
        indices3 = [i for i, s in enumerate(listoflists[4]) if 'Ocupancy' in s]
        occupancyApp = (listoflists[4][(indices3[0])])[11:-3]
        print(occupancyApp)
    except:
        occupancyApp = "Occupancy not found"
        print(occupancyApp)
        pass
    #This gets building class
    try:
        indices5 = [i for i, s in enumerate(listoflists[4]) if 'Building Class and Quality' in s]
        buildingClassApp = (listoflists[4][(indices5[0] + 1)])[5:-8]
        print(buildingClassApp)
    except:
        buildingClassApp = "Building Class not found"
        print(buildingClassApp)
        pass
    #This gets Quality
    try:
        qualityApp = (listoflists[4][(indices5[0] + 2)])[1:-4]
        print(qualityApp)
    except:
        qualityApp = "Quality not found"
        print(qualityApp)
        pass
    #This gets Age
    try:
        indices4 = [i for i, s in enumerate(listoflists[4]) if 'Age and condition' in s]
        ageApp = (listoflists[4][(indices4[0] + 1)])[3:-5]
        print(ageApp)
    except:
        ageApp = "Age not found"
        print(ageApp)
        pass
    #This gets condition
    try:
        conditionApp = (listoflists[4][(indices4[0] + 2)])[2:-4]
        print((listoflists[4][(indices4[0] + 2)])[2:-4])
    except:
        conditionApp = "Condition not found"
        print("Condition not found")
        pass

    def ocr_core(coverpage2):
    # uses Pillow's Image class to open the image and pytesseract to detect the string in the image
    #This is the default "lens" tesseract uses. I am using this to get tesseract to look at images differently
        text = pytesseract.image_to_string(Image.open(coverpage2))
        return text

    listoflists2 = []

    #iterates over file names and has tesseract print output
    for path in pathList:
        splitpath = re.split(':|\n|\|',ocr_core(path))
        #splitpath2 = [x.replace('\n', ' ') for x in splitpath]
        splitpath2 = list(filter(None, splitpath))
        listoflists2.append(splitpath2)
        #listoflists.append(splitpath2)
        #target and grab specific information HERE
    #print(listoflists2[2])
    #print(listoflists[2])
    #ATTENTION: You might want to individualize these values
    try:
        vacSaleHead = listoflists2[2].index('Value')
        vacSalePrim = (listoflists2[2][(vacSaleHead + 1)])
    #Gets Parcel Num
        vacSalePrimParcel = vacSalePrim[3:-12]
        print(vacSalePrimParcel)
    except:
        vacSalePrimParcel = "Parcel Number not found"
        print(vacSalePrimParcel)
        pass
    #Gets Sale Price
    try:
        vacSalePrimSale = (vacSalePrim[17:-1]).replace('$','').replace(',','')
        print(vacSalePrimSale)
    except:
        vacSalePrimSale = "Sale Price not found"
        print(vacSalePrimSale)
    #Gets Land Residual
    try:
        cost_appr_list1 = (listoflists2[2][(vacSaleHead + 3)]).replace('$','').replace(',','').split(' ')
        print(cost_appr_list1[1])
    except:
        cost_appr_list1 = "Land Residual not found"
        print(cost_appr_list1)
    #Gets Size
    try:
        primSize = cost_appr_list1[2]
        print(primSize)
    except:
        primSize = "Size not found"
        print(primSize)
        pass
    #Gets Price Per Sq Ft
    try:
        primPricePerSquare = cost_appr_list1[3]
        print(primPricePerSquare)
    except:
        primPricePerSquare = "Price per sq ft not found"
        print(primPricePerSquare)
        pass
    #Gets 2nd Parcel #
    try:
        costPar2 = (listoflists2[2][(vacSaleHead + 4)])[3:]
        print(costPar2)
    except:
        costPar2 = "2nd Parcel not found"
        print(costPar2)
        pass
    #Gets 2nd Sale price
    try:
        salePrice2 = (listoflists2[2][vacSaleHead + 7]).replace('$','').replace(',','')
        print(salePrice2)
    except:
        salePrice2 = "2nd Sale Price not found"
        print(salePrice2)
        pass
    #Gets 2nd Size
    try:
        size_list2 = (listoflists2[2][(vacSaleHead + 8)]).replace('$','').replace(',','').split(' ')
        secondarySize = size_list2[3]
        print(secondarySize)
    except:
        secondarySize = "2nd Size not found"
        print(secondarySize)
        pass
    #Gets 2nd Price per sq ft
    try:
        secondaryPricePerSquare = size_list2[4]
        print(secondaryPricePerSquare)
    except:
        secondaryPricePerSquare = "2nd Price per sq ft not found"
        print(secondaryPricePerSquare)
        pass
    #Gets 3rd Parcel #
    try:
        costPar3 = (listoflists2[2][(vacSaleHead + 9)])
        print(costPar3)
    except:
        costPar3 = "3rd Parcel not found"
        print(costPar3)
        pass
    #Gets 3rd Sale price
    try:
        salePrice3 = (listoflists2[2][(vacSaleHead + 12)]).replace('$','').replace(',','')
        print(salePrice3)
    except:
        salePrice3 = "3rd Sale Price not found"
        print(salePrice3)
        pass
    #Gets 3rd Size
    try:
        size_list3 = (listoflists2[2][(vacSaleHead + 13)]).replace('$','').replace(',','').split(' ')
        tertSize = size_list3[3]
        print(tertSize)
    except:
        tertSize = "3rd Size not found"
        print(tertSize)
        pass
    #Gets 3rd Price per sq ft
    try:
        tertPricePerSquare = size_list3[4]
        print(tertPricePerSquare)
    except:
        tertPricePerSquare = "3rd Price per sq ft not found"
        print(tertPricePerSquare)
        pass

    #Find a way to get each data st in table without having to individually grab the info. Might be difficult because of varying vacant sales
    #Gets price per sqft
    try:
        indices5 = [i for i, s in enumerate(listoflists2[2]) if 'Price per SqFt' in s]
        sqftApp = (listoflists2[2][(indices5[0])])[15:].replace('$','').replace(',','')
        print(sqftApp)
    except:
        sqftApp = "Price per Square Foot not found"
        print(sqftApp)
    #price_per_sqft_head = listoflists2[2].index('Price per SqFt')
    #print(price_per_sqft_head[15:].replace('$',''))
    #Gets estimated building improvements
    try:
        indices6 = [i for i, s in enumerate(listoflists2[2]) if 'Estimated Building' in s]
        buildImprApp = (listoflists2[2][(indices6[0])])[74:].replace('$','').replace(',','')
        print(buildImprApp)
    except:
        buildImprApp = "Estimated Building Improvements not found"
        print(buildImprApp)
    #Gets extra ft. val
    try:
        ftvalHead = listoflists2[2].index('PA Miscellaneous Extra Feature Value')
        ftvalPrim = ((listoflists2[2][(ftvalHead + 1)])[1:].replace('$','').replace(',',''))
        print(ftvalPrim)
    except:
        ftvalPrim = "PA Miscellaneous Extra Feature Value not found"
        print(ftvalPrim)
        pass
    #Gets estimated land value
    try:
        indices7 = [i for i, s in enumerate(listoflists2[2]) if 'Estimated Land Value' in s]
        landValApp = (listoflists2[2][(indices7[0])])[53:].replace('$','').replace(',','')
        print(landValApp)
    except:
        landValApp = "Estimated Land Value not found"
        print(landValApp)
    #Gets total cost approach
    try:
        indices8 = [i for i, s in enumerate(listoflists2[2]) if 'Total Cost Approach' in s]
        totalCostAppVar = (listoflists2[2][(indices8[0])])[20:].replace('$','').replace(',','')
        print(totalCostAppVar)
    except:
        totalCostAppVar = "Total Cost Approach not found"
        print(totalCostAppVar)
    #Gets prop appr market val
    try:
        indices9 = [i for i, s in enumerate(listoflists2[2]) if 'Market Value' in s]
        marketValApp = (listoflists2[2][(indices9[0] + 1)])[1:].replace('$','').replace(',','')
        print(marketValApp)
    except:
        marketValApp = "Property Appraiser Market Value not found"
        print(marketValApp)

    #On Income Approach Section
    #Gets Potential Gross Income
    try:
        indices10 = [i for i, s in enumerate(listoflists[8]) if 'Potential Gross Income' in s]
        potentialGrossIncome = (listoflists[8][(indices10[0])]).replace('Potential Gross Income','')
        print(potentialGrossIncome)
    except:
        potentialGrossIncome = "Potential Gross Income not found"
        print(potentialGrossIncome)
    #Gets Less Vacancies & Collections
    try:
        indices11 = [i for i, s in enumerate(listoflists[8]) if 'Less Vacanc' in s]
        lessVacancies = (listoflists[8][(indices11[0])]).replace('Less Vacancies & Collections','').replace('Less Vacancy and Collections', '')
        print(lessVacancies)
    except:
        lessVacancies = "Less Vacancies & Collections not found"
        print(lessVacancies)
    #Gets Effective Gross Income
    try:
        indices12 = [i for i, s in enumerate(listoflists[8]) if 'Effective Gross Income' in s]
        effectiveGrossIncome = (listoflists[8][(indices12[0])]).replace('Effective Gross Income','')
        print(effectiveGrossIncome)
    except:
        effectiveGrossIncome = "Effective Gross Income not found"
        print(effectiveGrossIncome)
    #Gets Less Operating Expenses
    try:
        indices13 = [i for i, s in enumerate(listoflists[8]) if 'Less Operating Expenses' in s]
        lessOperatingExpenses = (listoflists[8][(indices13[0])]).replace('Less Operating Expenses','')
        print(lessOperatingExpenses)
    except:
        lessOperatingExpenses = "Less Operating Expenses not found"
        print(lessOperatingExpenses)
    #Gets Net Operating Income
    try:
        indices14 = [i for i, s in enumerate(listoflists[8]) if 'Net Operating Income' in s]
        netOperatingIncome = (listoflists[8][(indices14[0])]).replace('Net Operating Income','')
        print(netOperatingIncome)
    except:
        netOperatingIncome = "Net Operating Income not found"
        print(netOperatingIncome)
    #Gets Cap Rate
    try:
        indices15 = [i for i, s in enumerate(listoflists[8]) if 'Cap Rate' in s]
        capRate = (listoflists[8][(indices15[0])]).replace('Cap Rate','')
        print(capRate)
    except:
        capRate = "Cap Rate not found"
        print(capRate)
    #Gets Plus Effective Tax Rate
    try:
        indices16 = [i for i, s in enumerate(listoflists[8]) if 'Plus Effective Tax Rate' in s]
        plusEffectiveTaxRate = (listoflists[8][(indices16[0])]).replace('Plus Effective Tax Rate','')
        print(plusEffectiveTaxRate)
    except:
        plusEffectiveTaxRate = "Plus Effective Tax Rate not found"
        print(plusEffectiveTaxRate)
    #Gets Overall Rate
    try:
        indices17 = [i for i, s in enumerate(listoflists[8]) if 'Overall Rate' in s]
        OverallRate = (listoflists[8][(indices17[0])]).replace('Overall Rate','')
        print(OverallRate)
    except:
        OverallRate = "Overall Rate not found"
        print(OverallRate)
    #Gets Estimated Market Value
    try:
        indices18 = [i for i, s in enumerate(listoflists[8]) if 'Estimated Market' in s]
        EstimatedMarket = (listoflists[8][(indices18[0])]).replace('Estimated Market Value','')
        print(EstimatedMarket)
    except:
        EstimatedMarket = "Estimated Market Value not found"
        print(EstimatedMarket)

    #print(listoflists2[5])
    #print(listoflists[5])
    #try:
        #print(listoflists2[8])
        #print(listoflists[8])
    #except:
        #pass

    import global_count
    global_count.incrementFunc()

    with open('vabData.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if open('log.txt').read() == "1":
            writer.writerow(["id", "parcel", "roll", "petition", "pacs", "zoning", "tang", "cost", "sale", "income", "occupancy", "build", "quality", "age", "condition", "priceSquare", "buildImpr", "extraFeature", "estLandVal", "totalCostAppr", "propApprMarketVal", "potentialGrossIncome", "lessVacanciesandCollections", "effectiveGrossIncome", "lessOperatingExpenses", "netOperatingIncome", "capRate", "plusEffectiveTaxRate", "overallRate", "estimatedMarketVal", "cost_comp1_parcel", "cost_comp1_sale_price", "cost_comp1_size", "cost_comp1_price_per_square", "cost_comp2_parcel", "cost_comp2_sale_price", "cost_comp2_size", "cost_comp2_price_per_square", "cost_comp3_parcel", "cost_comp3_sale_price", "cost_comp3_size", "cost_comp3_price_per_square"])
            #if all([var1, var2, var3, var4]):
        writer.writerow([open('log.txt').read(), parcelNumVar, rollYearVar, petitionNumVar, imprDataVar.replace(',',''), zoningVar, tangVar, costVar, salesMinVar + " " + salesMaxVar, incomeApp3, occupancyApp, buildingClassApp, qualityApp, ageApp, conditionApp, sqftApp, buildImprApp, ftvalPrim, landValApp, totalCostAppVar, marketValApp, potentialGrossIncome, lessVacancies, effectiveGrossIncome, lessOperatingExpenses, netOperatingIncome, capRate, plusEffectiveTaxRate, OverallRate, EstimatedMarket, vacSalePrimParcel, vacSalePrimSale, primSize, primPricePerSquare, costPar2, salePrice2, secondarySize, secondaryPricePerSquare, costPar3, salePrice3, tertSize, tertPricePerSquare])

    for filename in os.listdir(r'C:\Users\mclark\Desktop\python\flask'):
        if filename.endswith('.png'):
            os.remove(filename)
            continue
        else:
            continue

    for filename in os.listdir(r'C:\Users\mclark\Desktop\python\flask'):
        if filename.endswith('.pdf'):
            os.remove(filename)
            continue
        else:
            continue
