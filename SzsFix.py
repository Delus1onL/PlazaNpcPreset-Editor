#By Delus1on_L

with open('PlayerInfo.szs', 'rb') as originalSzs:
    with open('Output/PlayerInfo.szs', 'wb') as newSzs:
    
        first_chunk = originalSzs.read(8)
        newSzs.write(first_chunk)
        
        data_size = 4
        dataSectionAlign = originalSzs.read(data_size)
        intDataSectionAlign = int.from_bytes(dataSectionAlign)
        print(intDataSectionAlign)
        intDataSectionAlign = 8192
        dataSectionAlign = intDataSectionAlign.to_bytes(4, "big")
        newSzs.write(dataSectionAlign)
        dataSection = originalSzs.read(data_size)

        while len(dataSection) > 0:
            newSzs.write(dataSection)
            
            dataSection = originalSzs.read(data_size)

