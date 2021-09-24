from User import User

adrienUser = User( "Adrien" )
adrienUser.account['OtherSavings'].deposite( 100 ).deposite( 300 ).withdraw ( 500 )
adrienUser.account['Savings'].deposite( 200 ).deposite( 6000 ).withdraw ( 100 )
adrienUser.printInfo()