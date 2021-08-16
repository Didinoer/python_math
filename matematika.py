def instruksi () :
    print("""daftar isi module yang dapat digunakan yaitu :
    - tambah(nilai1,nilai2) 
    - kurang(nilai1,nilai2) 
    - perkalian(nilai1,nilai2)
    - pembagian(nilai1,nilai2) 
    - modulus(nilai1,nilai2)
    - penjumlahan_deret(nilai)
    - faktorial(nilai) note: untuk menampilkan wajib pakai print""")


def tambah (num1,num2) :
  result = num1 +num2 
  print( num1, "+", num2 , "=" ,result)
  return result
   
def kurang (num1,num2) :
    result = num1-num2 
    print(num1, "+",num2, "=" ,result)
    return result
def perkalian (num1,num2) :
    result = num1 * num2 
    print(num1, "X",num2, "=" ,result)
    return result

def pembagian (num1,num2) :
    result = num1/num2 
    print(num1, "/",num2, "=" ,result)
    return result



def modulus (num1,num2) :
    result = num1 % num2 
    print(num1, "%",num2, "=" ,result)  
    return result
   

def penjumlahan_deret(n):
    for i in range (n) : z= (n+1)/2 * n 
    print(" penjumlahan deret dari 1 sampai ", n , "=",z )
    return z


def faktorial(n) :
     if n ==1 :
         return 1
     else :
         print(n, "\n X")
         return n*faktorial(n-1)
         
