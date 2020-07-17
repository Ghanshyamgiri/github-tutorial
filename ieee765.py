def Input_Register():
    for i in range(1,3):
        First_Value=int(input(f'Enter Input Register Value {i}: '))
        First_Value1=str(First_Value)
        if First_Value<0:
                Input_Regi=First_Value1[:6]
        else:Input_Regi=First_Value1[:5]
        print(Input_Regi)
Input_Register()