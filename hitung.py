def jumlah(a):                
    #nama-nama satuan
    nm1="batang"
    nm2="bungkus"
    nm3="slop"
    nm4="ball"
    nm5="palet"
    
    #jumlah satuan masing-masing dalam pieces
    qty1=1            #1 batang
    qty2=12            #12 batang = 1 bungkus
    qty3=120        #120 batang = 1 slop
    qty4=2880        #2880 batang = 1 ball
    qty5=69120    #69120 batang = 1 palet
    over=0            #gak ada satuannya, buat pembates
    
    #bikin variabel tampil1 sampai tampil5
    for i in range(1,6):
        exec "tampil"+str(i)+"=''"
    
    #------------------------------------------------------
    #rumus buat menghitung satuan berdasarkan nilai modulus
    #------------------------------------------------------
    if over<qty5:
        nmqty5=(a/qty5)
    elif qty5!=0:
        nmqty5=((a%over/qty5))
    else:
        nmqty5=0        
    
    if qty5<qty4:
        nmqty4=(a/qty4)                    
    elif qty5!=0:
        nmqty4=((a%qty5)/qty4)            
    else:
        nmqty4=0                
    
    if qty4<qty3:
        nmqty3=(a/qty3)
    elif qty4!=0:
        nmqty3=((a%qty4)/qty3)
    else:
        nmqty3=0
        
    if qty3<qty2:
        nmqty2=(a/qty2)
    elif qty3!=0:    
        nmqty2=((a%qty3)/qty2)
    else:
        nmqty2=0

    nmqty1=(a%qty2)
    #------------------------------------------------------
    
    #------------------------------------------------------
    #rumus biar program gak menampilkan satuan yang hailnya 0
    #------------------------------------------------------    
    if nmqty5!=0:
        tampil5=str(nmqty5)+" "+nm5+", "
        
    if nmqty4!=0:
        tampil4=str(nmqty4)+" "+nm4+", "
        
    if nmqty3!=0:
        tampil3=str(nmqty3)+" "+nm3+", "
        
    if nmqty2!=0:
        tampil2=str(nmqty2)+" "+nm2+", "
        
    if nmqty1!=0:
        tampil1=str(nmqty1)+" "+nm1
    #------------------------------------------------------

    
    #tampilkan hasil
    print ""    
    tampil=tampil5+tampil4+tampil3+tampil2+tampil1
    print tampil
    
a=raw_input("Masukkan qty dalam pieces : ")
jumlah(int(a))