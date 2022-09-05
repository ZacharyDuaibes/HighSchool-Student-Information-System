studentNumber = []
firstName = []
lastName = []
studentGrade = []

import random
firstNames = ['Liam', 'Noah', 'Oliver', 'Elijah', 'Lucas', 'Levi', 'Mason', 'Asher', 'James', 'Ethan', 'Mateo', 
            'Leo', 'Jack', 'Benjamin', 'Aiden', 'Logan', 'Grayson', 'Jackson', 'Henry', 'Wyatt', 'Sebastian', 'Carter', 
            'Daniel', 'William', 'Alexander', 'Ezra', 'Owen', 'Michael', 'Muhammad', 'Julian', 'Hudson', 'Luke', 'Samuel', 
            'Jacob', 'Lincoln', 'Gabriel', 'Jaden', 'Luca', 'Maverick', 'David', 'Josiah', 'Elias', 'Jaxon', 'Kai', 'Anthony', 
            'Isaiah', 'Eli', 'John', 'Joseph', 'Matthew', 'Ezekiel', 'Adam', 'Caleb', 'Isaac', 'Theodore', 'Nathan', 'Theo', 
            'Thomas', 'Nolan', 'Waylon', 'Ryan', 'Easton', 'Roman', 'Adrian', 'Miles', 'Greyson', 'Cameron', 'Colton', 'Landon', 
            'Santiago', 'Andrew', 'Hunter', 'Jameson', 'Joshua', 'Jace', 'Cooper', 'Dylan', 'Jeremiah', 'Kingston', 'Xavier', 
            'Christian', 'Kayden', 'Charlie', 'Aaron', 'Jaxson', 'Silas', 'Ryder', 'Austin', 'Dominic', 'Amir', 
            'Carson', 'Jordan', 'Weston', 'Micah', 'Rowan', 'Beau', 'Declan', 'Everett', 'Alex', 'Bennett', 'Declan', 'Waylon', 
            'Weston', 'Evan', 'Emmett', 'Micah', 'Ryder', 'Beau', 'Damian', 'Brayden', 'Gael', 'Rowan', 'Harrison', 'Bryson', 
            'Sawyer', 'Amir', 'Kingston', 'Jason', 'Giovanni', 'Vincent', 'Ayden', 'Chase', 'Myles', 'Diego', 'Nathaniel', 
            'Legend', 'Jonah', 'River', 'Tyler', 'Cole', 'Braxton', 'George', 'Milo', 'Zachary', 'Ashton', 'Luis', 'Jasper', 
            'Kaiden', 'Adriel', 'Gavin', 'Bentley', 'Calvin', 'Zion', 'Juan', 'Maxwell', 'Max', 'Ryker', 'Carlos', 'Emmanuel', 
            'Olivia', 'Emma', 'Amelia', 'Ava', 'Sophia', 'Charlotte', 'Isabella', 'Mia', 'Luna', 'Harper', 'Gianna', 'Evelyn', 
            'Aria', 'Ella', 'Ellie', 'Mila', 'Layla', 'Avery', 'Camila', 'Lily', 'Scarlett', 'Sofia', 'Nova', 'Aurora', 
            'Chloe', 'Riley', 'Nora', 'Hazel', 'Abigail', 'Rylee', 'Penelope', 'Elena', 'Zoey', 'Isla', 'Elanor', 'Elizabeth', 
            'Madison', 'Willow', 'Emilia', 'Violet', 'Emily', 'Eliana', 'Stella', 'Maya', 'Paisley', 'Everly', 'Addison', 
            'Ryleigh', 'Ivy', 'Grace', 'Hannah', 'Bella', 'Naomi', 'Zoe', 'Aaliyah', 'Kinsley', 'Lucy', 'Delilah', 'Skylar', 
            'Leilani', 'Ayla', 'Victoria', 'Alice', 'Aubrey', 'Savannah', 'Serenity', 'Autumn', 'Leah', 'Sophie', 'Natalie', 
            'Athena', 'Lillian', 'Hailey', 'Audrey', 'Eva', 'Everleigh', 'Kennedy', 'Maria', 'Natalia', 'Nevaeh', 'Brooklyn', 
            'Raelynn', 'Arya', 'Ariana', 'Madelyn', 'Claire', 'Valentina', 'Sadie', 'Gabriella', 'Ruby', 'Anna', 'Iris', 
            'Charlie', 'Brielle', 'Emery','Melody', 'Amara', 'Piper', 'Quinn', 'Jade', 'Vivian', 'Rylee', 'Clara', 'Raelynn', 
            'Melanie', 'Melody', 'Julia', 'Athena', 'Maria', 'Liliana', 'Hadleey', 'Arya', 'Rose', 'Reagan', 'Eliza', 'Adalynn', 
            'Kaylee', 'Lyla', 'Mackenzie', 'Alaia', 'Isabelle', 'Charlie', 'Arianna', 'Mary', 'Remi', 'Margaret', 'Iris', 
            'Parker', 'Ximena', 'Eden', 'Ayla', 'Kylie', 'Elliana', 'Josie', 'Katherine', 'Faith', 'Alexandria', 'Eloise', 
            'Adalyn', 'Amaya', 'Jasmine', 'Amara', 'Daisy', 'Reese', 'Valerie', 'Brianna', 'Cecilia', 'Andrea', 'Summer', 
            'Valeria']

lastNames = ['SMITH', 'JOHNSON', 'WILLIAMS', 'BROWN', 'JONES', 'GARCIA', 'MILLER', 'DAVIS', 'RODRIGUEZ',
             'MARTINEZ', 'HERNANDEZ', 'LOPEZ', 'GONZALEZ', 'WILSON', 'ANDERSON', 'THOMAS', 'TAYLOR',
             'MOORE', 'JACKSON', 'MARTIN', 'LEE', 'PEREZ', 'THOMPSON', 'WHITE', 'HARRIS', 'SANCHEZ',
             'CLARK', 'RAMIREZ', 'LEWIS', 'ROBINSON', 'WALKER', 'YOUNG', 'ALLEN', 'KING', 'WRIGHT',
             'SCOTT', 'TORRES', 'NGUYEN', 'HILL', 'FLORES', 'GREEN', 'ADAMS', 'NELSON', 'BAKER', 'HALL',
             'RIVERA', 'CAMPBELL', 'MITCHELL', 'CARTER', 'ROBERTS', 'GOMEZ', 'PHILLIPS', 'EVANS', 'TURNER',
             'DIAZ', 'PARKER', 'CRUZ', 'EDWARDS', 'COLLINS', 'REYES', 'STEWART', 'MORRIS', 'MORALES',
             'MURPHY', 'COOK', 'ROGERS', 'GUTIERREZ', 'ORTIZ', 'MORGAN', 'COOPER', 'PETERSON', 'BAILEY',
             'REED', 'KELLY', 'HOWARD', 'RAMOS', 'KIM', 'COX', 'WARD', 'RICHARDSON', 'WATSON', 'BROOKS',
             'CHAVEZ', 'WOOD', 'JAMES', 'BENNETT', 'GRAY', 'MENDOZA', 'RUIZ', 'HUGHES', 'PRICE', 'ALVAREZ',
             'CASTILLO', 'SANDERS', 'PATEL', 'MYERS', 'LONG', 'ROSS', 'FOSTER', 'JIMENEZ', 'POWELL',
             'JENKINS', 'PERRY', 'RUSSELL', 'SULLIVAN', 'BELL', 'COLEMAN', 'BUTLER', 'HENDERSON', 'BARNES',
             'GONZALES', 'FISHER', 'VASQUEZ', 'SIMMONS', 'ROMERO', 'JORDAN', 'PATTERSON', 'ALEXANDER',
             'HAMILTON', 'GRAHAM', 'REYNOLDS', 'GRIFFIN', 'WALLACE', 'MORENO', 'WEST', 'COLE', 'HAYES',
             'BRYANT', 'HERRERA', 'GIBSON', 'ELLIS', 'TRAN', 'MEDINA', 'AGUILAR', 'STEVENS', 'MURRAY',
             'FORD', 'CASTRO', 'MARSHALL', 'OWENS', 'HARRISON', 'FERNANDEZ', 'McDONALD', 'WOODS',
             'WASHINGTON', 'KENNEDY', 'WELLS', 'VARGAS', 'HENRY', 'CHEN', 'FREEMAN', 'WEBB', 'TUCKER',
             'GUZMAN', 'BURNS', 'CRAWFORD', 'OLSON', 'SIMPSON', 'PORTER', 'HUNTER', 'GORDON', 'MENDEZ',
             'SILVA', 'SHAW', 'SNYDER', 'MASON', 'DIXON', 'MUÑOZ', 'HUNT', 'HICKS', 'HOLMES', 'PALMER',
             'WAGNER', 'BLACK', 'ROBERTSON', 'BOYD', 'ROSE', 'STONE', 'SALAZAR', 'FOX', 'WARREN', 'MILLS',
             'MEYER', 'RICE', 'SCHMIDT', 'GARZA', 'DANIELS', 'FERGUSON', 'NICHOLS', 'STEPHENS', 'SOTO',
             'WEAVER', 'RYAN', 'GARDNER', 'PAYNE', 'GRANT', 'DUNN', 'KELLEY', 'SPENCER', 'HAWKINS',
             'ARNOLD', 'PIERCE', 'VAZQUEZ', 'HANSEN', 'PETERS', 'SANTOS', 'HART', 'BRADLEY', 'KNIGHT',
             'ELLIOTT', 'CUNNINGHAM', 'DUNCAN', 'ARMSTRONG', 'HUDSON', 'CARROLL', 'LANE', 'RILEY',
             'ANDREWS', 'ALVARADO', 'RAY', 'DELGADO', 'BERRY', 'PERKINS', 'HOFFMAN', 'JOHNSTON',
             'MATTHEWS', 'PEÑA', 'RICHARDS', 'CONTRERAS', 'WILLIS', 'CARPENTER', 'LAWRENCE', 'SANDOVAL',
             'GUERRERO', 'GEORGE', 'CHAPMAN', 'RIOS', 'ESTRADA', 'ORTEGA', 'WATKINS', 'GREENE', 'NUÑEZ',
             'WHEELER', 'VALDEZ', 'HARPER', 'BURKE', 'LARSON', 'SANTIAGO', 'MALDONADO', 'MORRISON',
             'FRANKLIN', 'CARLSON', 'AUSTIN', 'DOMINGUEZ', 'CARR', 'LAWSON', 'JACOBS', 'O’BRIEN', 'LYNCH',
             'SINGH', 'VEGA', 'BISHOP', 'OLIVER', 'JENSEN', 'HARVEY', 'WILLIAMSON', 'ALEXANDER',
             'GILBERT', 'DEAN', 'SIMS', 'ESPINOZA', 'HOWELL', 'LI', 'WONG', 'REID', 'HANSON', 'LE',
             'McCOY', 'GARRETT', 'BURTON', 'FULLER', 'WANG', 'WEBER', 'WELCH', 'ROJAS', 'LUCAS', 'MARQUEZ',
             'FIELDS', 'PARK', 'YANG', 'LITTLE', 'BANKS', 'PADILLA', 'DAY', 'WALSH', 'BOWMAN', 'SCHULTZ',
             'LUNA', 'FOWLER', 'MEJIA', 'DAVIDSON', 'ACOSTA', 'BREWER', 'MAY', 'HOLLAND', 'JUAREZ',
             'NEWMAN', 'PEARSON', 'CURTIS', 'CORTÉZ', 'DOUGLAS', 'SCHNEIDER', 'JOSEPH', 'BARRETT',
             'NAVARRO', 'FIGUEROA', 'KELLER', 'ÁVILA', 'WADE', 'MOLINA', 'STANLEY', 'HOPKINS', 'CAMPOS',
             'BARNETT', 'BATES', 'CHAMBERS', 'CALDWELL', 'BECK', 'LAMBERT', 'MIRANDA', 'BYRD', 'CRAIG',
             'AYALA', 'LOWE', 'FRAZIER', 'POWERS', 'NEAL', 'LEONARD', 'GREGORY', 'CARRILLO', 'SUTTON',
             'FLEMING', 'RHODES', 'SHELTON', 'SCHWARTZ', 'NORRIS', 'JENNINGS', 'WATTS', 'DURAN',
             'WALTERS', 'COHEN', 'McDANIEL', 'MORAN', 'PARKS', 'STEELE', 'VAUGHN', 'BECKER', 'HOLT',
             'DELEON', 'BARKER', 'TERRY', 'HALE', 'LEON', 'HAIL', 'BENSON', 'HAYNES', 'HORTON', 'MILES',
             'LYONS', 'PHAM', 'GRAVES', 'BUSH', 'THORNTON', 'WOLFE', 'WARNER', 'CABRERA', 'McKINNEY',
             'MANN', 'ZIMMERMAN', 'DAWSON', 'LARA', 'FLETCHER', 'Pgrade', 'McCARTHY', 'LOVE', 'ROBLES',
             'CERVANTES', 'SOLIS', 'ERICKSON', 'REEVES', 'CHANG', 'KLEIN', 'SALINAS', 'FUENTES',
             'BALDWIN', 'DANIEL', 'SIMON', 'VELASQUEZ', 'HARDY', 'HIGGINS', 'AGUIRRE', 'LIN',
             'CUMMINGS', 'CHANDLER', 'SHARP', 'BARBER', 'BOWEN', 'OCHOA', 'DENNIS', 'ROBBINS', 'LIU',
             'RAMSEY', 'FRANCIS', 'GRIFFITH', 'PAUL', 'BLAIR', 'O’CONNOR', 'CARDENAS', 'PACHECO',
             'CROSS', 'CALDERON', 'QUINN', 'MOSS', 'SWANSON', 'CHAN', 'RIVAS', 'KHAN', 'RODGERS',
             'SERRANO', 'ROSALES', 'STEVENSON', 'CHRISTENSEN', 'MANNING', 'GILL', 'CURRY',
             'McLAUGHLIN', 'HARMON', 'McGEE', 'GROSS', 'DOYLE', 'GARNER', 'NEWTON', 'BURGESS', 'REESE',
             'WALTON', 'BLAKE', 'TRUJILLO', 'ADKINS', 'BRADY', 'GOODMAN', 'ROMAN', 'WEBSTER', 'GOODWIN',
             'FISCHER', 'HUANG', 'POTTER', 'DELACRUZ', 'MONTOYA', 'TODD', 'WU', 'HINES', 'MULLINS',
             'CASTANEDA', 'MALONE', 'CANNON', 'TATE', 'MACK', 'SHERMAN', 'HUBBARD', 'HODGES', 'ZHANG',
             'GUERRA', 'WOLF', 'VALENCIA', 'SAUNDERS', 'FRANCO', 'ROWE', 'GALLAGHER', 'FARMER', 'HAMMOND',
             'HAMPTON', 'TOWNSEND', 'INGRAM', 'WISE', 'GALLEGOS', 'CLARKE', 'BARTON', 'SCHROEDER',
             'MAXWELL', 'WATERS', 'LOGAN', 'CAMACHO', 'STRICKLAND', 'NORMAN', 'PERSON', 'COLÓN',
             'PARSONS', 'FRANK', 'HARRINGTON', 'GLOVER', 'OSBORNE', 'BUCHANAN', 'CASEY', 'FLOYD',
             'PATTON', 'IBARRA', 'BALL', 'TYLER', 'SUAREZ', 'BOWERS', 'OROZCO', 'SALAS', 'COBB', 'GIBBS',
             'ANDRADE', 'BAUER', 'CONNER', 'MOODY', 'ESCOBAR', 'McGUIRE', 'LLOYD', 'MUELLER', 'HARTMAN',
             'FRENCH', 'KRAMER', 'McBRIDE', 'POPE', 'LINDSEY', 'VELAZQUEZ', 'NORTON', 'McCORMICK',
             'SPARKS', 'FLYNN', 'YATES', 'HOGAN', 'MARSH', 'MACIAS', 'VILLANUEVA', 'ZAMORA', 'PRATT',
             'STOKES', 'OWEN', 'BALLARD', 'LANG', 'BROCK', 'VILLARREAL', 'CHARLES', 'DRAKE', 'BARRERA',
             'CAIN', 'PATRICK', 'PIÑEDA', 'BURNETT', 'MERCADO', 'SANTANA', 'SHEPHERD', 'BAUTISTA', 'ALI',
             'SHAFFER', 'LAMB', 'TREVINO', 'McKENZIE', 'HESS', 'BEIL', 'OLSEN', 'COCHRAN', 'MORTON',
             'NASH', 'WILKINS', 'PETERSEN', 'BRIGGS', 'SHAH', 'ROTH', 'NICHOLSON', 'HOLLOWAY', 'LOZANO',
             'RANGEL', 'FLOWERS', 'HOOVER', 'SHORT', 'ARIAS', 'MORA', 'VALENZUELA', 'BRYAN', 'MEYERS',
             'WEISS', 'UNDERWOOD', 'BASS', 'GREER', 'SUMMERS', 'HOUSTON', 'CARSON', 'MORROW', 'CLAYTON',
             'WHITAKER', 'DECKER', 'YODER', 'COLLIER', 'ZUNIGA', 'CAREY', 'WILCOX', 'MELENDEZ', 'POOLE',
             'ROBERSON', 'LARSEN', 'CONLEY', 'DAVENPORT', 'COPELAND', 'MASSEY', 'LAM', 'HUFF', 'ROCHA',
             'CAMERON', 'JEFFERSON', 'HOOD', 'MONROE', 'ANTHONY', 'PITTMAN', 'HUYNH', 'RANDALL',
             'SINGLETON', 'KIRK', 'COMBS', 'MATHIS', 'CHRISTIAN', 'SKINNER', 'BRADFORD', 'RICHARD',
             'GALVAN', 'WALL', 'BOONE', 'KIRBY', 'WILKINSON', 'BRIDGES', 'BRUCE', 'ATKINSON', 'VELEZ',
             'MEZA', 'ROY', 'VINCENT', 'YORK', 'HODGE', 'VILLA', 'ABBOTT', 'ALLISON', 'TAPIA', 'GATES',
             'CHASE', 'SOSA', 'SWEENEY', 'FARRELL', 'WYATT', 'DALTON', 'HORN', 'BARRON', 'PHELPS', 'YU',
             'DICKERSON', 'HEATH', 'FOLEY', 'ATKINS', 'MATHEWS', 'BONILLA', 'ACEVEDO', 'BENITEZ',
             'ZAVALA', 'HENSLEY', 'GLENN', 'CISNEROS', 'HARRELL', 'SHIELDS', 'RUBIO', 'HUFFMAN', 'CHOI',
             'BOYER', 'GARRISON', 'ARROYO', 'BOND', 'KANE', 'HANCOCK', 'CALLAHAN', 'DILLON', 'CLINE',
             'WIGGINS', 'GRIMES', 'ARELLANO', 'MELTON', 'O’NEILL', 'SAVgrade', 'HO', 'BELTRAN', 'PITTS',
             'PARRISH', 'PONCE', 'RICH', 'BOOTH', 'KOCH', 'GOLDEN', 'WARE', 'BRENNAN', 'McDOWELL',
             'MARKS', 'CANTU', 'HUMPHREY', 'BAXTER', 'SAWYER', 'CLAY', 'TANNER', 'HUTCHINSON', 'KAUR',
             'BERG', 'WILEY', 'GILMORE', 'RUSSO', 'VILLEGAS', 'HOBBS', 'KEITH', 'WILKERSON', 'AHMED',
             'BEARD', 'McCLAIN', 'MONTES', 'MATA', 'ROSARIO', 'VANG', 'WALTER', 'HENSON', 'O’NEAL',
             'MOSLEY', 'McCLURE', 'BEASLEY', 'STEPHENSON', 'SNOW', 'HUERTA', 'PRESTON', 'VANCE', 'BARRY',
             'JOHNS', 'EATON', 'BLACKWELL', 'DYER', 'PRINCE', 'MACDONALD', 'SOLOMON', 'GUEVARA',
             'STAFFORD', 'ENGLISH', 'HURST', 'WOODARD', 'CORTES', 'SHANNON', 'KEMP', 'NOLAN',
             'MERRITT', 'MURILLO', 'MOON', 'SALGADO', 'STRONG', 'KLINE', 'CORDOVA', 'DAUGHERTY',
             'BARAJAS', 'ROACH', 'ROSAS', 'WINTERS', 'JACOBSON', 'LESTER', 'KNOX', 'BULLOCK', 'KERR',
             'LEACH', 'MEADOWS', 'ORR', 'DAVILA', 'WHITEHEAD', 'PRUITT', 'KENT', 'CONWAY', 'McKEE',
             'BARR', 'DAVID', 'DEJESUS', 'MARIN', 'BERGER', 'McINTYRE', 'GAINES','PALACIOS', 'CUEVAS',
             'BARTLETT', 'DURHAM', 'DORSEY', 'McCALL', 'O’DONNELL', 'STEIN', 'FAULKNER',
             'BROWNING', 'STOUT', 'LOWERY', 'SLOAN', 'McLEAN', 'HENDRICKS', 'CALHOUN', 'SEXTON', 'CHUNG',
             'GENTRY', 'HULL', 'DUARTE', 'ELLISON', 'NIELSEN', 'GILLESPIE', 'BUCK', 'MIDDLETON',
             'SELLERS', 'LEBLANC', 'ESPARZA', 'HARDIN', 'BRADSHAW', 'McINTOSH', 'HOWE', 'LIVINGSTON',
             'FROST', 'GLASS', 'MORSE', 'KNAPP', 'HERMAN', 'STARK', 'BRAVO', 'NOBLE', 'SPEARS', 'WEEKS',
             'CORONA', 'FREDERICK', 'BUCKLEY', 'McFARLAND', 'HEBERT', 'ENRIQUEZ', 'HICKMAN', 'QUINTERO',
             'RANDOLPH', 'SCHAEFER', 'WALLS', 'TREJO', 'HOUSE', 'REILLY', 'MICHAEL', 'BRENNAN',
             'CONRAD', 'GILES', 'BENJAMIN', 'CROSBY', 'FITZPATRICK', 'DONOVAN', 'MAYS', 'MAHONEY',
             'VALENTINE', 'RAYMOND', 'MEDRANO', 'HAHN', 'McMILLAN', 'SMALL', 'BENTLEY', 'FELIX', 'PECK',
             'LUCERO', 'BOYLE', 'HANNA', 'PACE', 'RUSH', 'HURLEY', 'HARDING', 'McCONNELL', 'BERNAL',
             'NAVA', 'AYERS', 'EVERETT', 'VENTURA', 'AVERY', 'PUGH', 'MAYER', 'BENDER', 'SHEPARD',
             'McMAHON', 'LANDRY', 'CASE', 'SAMPSON', 'MOSES', 'MAGANA', 'BLACKBURN', 'DUNLAP', 'GOULD',
             'DUFFY', 'VAUGHAN', 'HERRING', 'McKAY', 'ESPINOSA', 'RIVERS', 'FARLEY', 'BERNARD', 'ASHLEY',
             'FRIEDMAN', 'POTTS', 'TRUONG', 'COSTA', 'CORREA', 'BLEVINS', 'NIXON', 'CLEMENTS', 'FRY',
             'DELAROSA', 'BEST', 'BENTON', 'LUGO', 'PORTILLO', 'DOUGHERTY', 'CRANE', 'HALEY', 'PHAN',
             'VILLALOBOS', 'BLANCHARD', 'HORNE', 'FINLEY', 'QUINTANA', 'LYNN', 'ESQUIVEL', 'BEAN',
             'DODSON', 'MULLEN', 'XIONG', 'HAYDEN', 'CANO', 'LEVY', 'HUBER', 'RICHMOND', 'MOYER', 'LIM',
             'FRYE', 'SHEPPARD', 'McCARTY', 'AVALOS', 'BOOKER', 'WALLER', 'PARRA', 'WOODWARD',
             'JARAMILLO', 'KRUEGER', 'RASMUSSEN', 'BRANDT', 'PERALTA', 'DONALDSON', 'STUART', 
             'MAYNARD', 'GALINDO', 'COFFEY', 'ESTES', 'SANFORD', 'BURCH', 'MADDOX', 'VO', 'O’CONNELL',
             'VU', 'ANDERSEN', 'SPENCE', 'McPHERSON', 'CHURCH', 'SCHMITT', 'STANTON', 'LEAL', 'CHERRY',
             'COMPTON', 'DUDLEY', 'SIERRA', 'POLLARD', 'ALFARO', 'HESTER', 'PROCTOR', 'LU', 'HINTON',
             'NOVAK', 'GOOD', 'MADDEN', 'McCANN', 'TERRELL', 'JARVIS', 'DICKSON', 'REYNA', 'CANTRELL',
             'MAYO', 'BRANCH', 'HENDRIX', 'ROLLINS', 'ROWLAND', 'WHITNEY', 'DUKE', 'ODOM',
             'TRAVIS', 'TANG', 'ARCHER']

#Creating the main menu
def menu():
    title = ("STUDENT INFORMATION SYSTEM")
    print(title.rjust(40))
    print(("=" * len(title)).rjust(40))
    print("\n(A)dd a student\n" + "(R)emove a student\n" + "(M)odify a student\n" + "(D)isplay students\n" + "(F)ind student number\n" + "(Q)uit\n")
    selection = input("Enter your selection: ").upper()
    
    #Calling a function depending on the user's input choice
    if selection == "D":
        printName()
    elif selection == "A":
        addAStudent()
    elif selection == "R":
        removeAStudent()
    elif selection == "M":    
        modifyAStudent()
    elif selection == "F":    
        findNumber()
    elif selection == "Q":
        quit()
    else:
        print("\nInvalid\n")
        menu()

#Creating random names
def randomStudents(Students):
        for i in range(Students):
            studentNumber.append(i+1)
            firstName.append(random.choice(firstNames))
            lastName.append(random.choice(lastNames).title())
            studentGrade.append(random.randint(9,12))

#Function for user input if choice is D 
def printName():
    print("\n")
    displayTitle = "DISPLAY STUDENTS" 
    print(displayTitle.rjust(33))
    print(("=" * len(displayTitle) + "\n").rjust(34))
    print("Display information for which grade?")
    grade = input("Enter the grade number or 'A' for all grades: ").upper()
    
    #Grade, All Students or Invalid check
    
    if grade == "A":
        print("\nSTUDENT #  NAME                 GRADE")
        printAll()
    
    elif grade == "9" or grade == "10" or grade == "11" or grade == "12":
        print("\nSTUDENT #  NAME                 GRADE")
        printGrade(grade)
        
    else:
        print("\nInvalid")
        menu()

#Function for user input if choice is R 
def removeAStudent():
    while True:
        print("\n")
        AddTitle = "REMOVE A STUDENT" 
        print(AddTitle.rjust(31))
        print(("=" * len(AddTitle) + "\n").rjust(32))
        removeNumber = input("Enter the student number of the student to remove: ")
        try:
            int(removeNumber)
            removeNumber = int(removeNumber)-1
                
        except:
            print("\nInvalid\n")
            menu()
        if removeNumber > len(firstName)-1:
            print("\nInvalid\n")
            menu()
        print("Remove", firstName[removeNumber], str(lastName[removeNumber]) + "?")
        yesOrNo = input("(Y)es or (N)o: ").upper()
        if yesOrNo == "N":
            menu()
        if yesOrNo != "N" and yesOrNo != "Y":
            print("\nInvalid\n")
            menu()
        if removeNumber < 0 or removeNumber >= len(firstName):
            print("\nInvalid\n")
            menu()
        print("\n",firstName[removeNumber], lastName[removeNumber], "has been removed\n\n")
        firstName.pop(removeNumber)
        lastName.pop(removeNumber) 
        studentGrade.pop(removeNumber)
        studentNumber.pop(removeNumber)
        menu()

#Function for user input if choice is A
def printAll():
    for i in range(len(studentNumber)):
        print(studentNumber[i],"".ljust(9-len(str(studentNumber[i]))),firstName[i],lastName[i].title(),"".ljust(18- (len(firstName[i])+(len(lastName[i])))),studentGrade[i])
    print("\nTotal students =",len(studentNumber),"\n\n")
    menu()

def printGrade(grade):
    count = 0
    for i in range(Students):
        if studentGrade[i] == int(grade):
            print(studentNumber[i],"".ljust(9-len(str(studentNumber[i]))),firstName[i],lastName[i].title(),"".ljust(18- (len(firstName[i])+(len(lastName[i])))),studentGrade[i])
            count += 1
        else:
            continue
    print("\nTotal students =",count,"\n\n")
    menu()
    
def addAStudent():
    while True:
        print("\n")
        AddTitle = "ADD A STUDENT" 
        print(AddTitle.rjust(31))
        print(("=" * len(AddTitle) + "\n").rjust(32))
        newFirstName = input("Enter the first name: ").title()
        if newFirstName.isalpha() == False:
            print("\nInvalid\n")
            menu()
        newLastName = input("Enter the last name: ").title()
        if newLastName.isalpha() == False:
            print("\nInvalid\n")
            menu()
        newGrade = input("Enter the grade: ")
        try:
            int(newGrade)
            newGrade= int(newGrade)
        except:
            print("\nInvalid\n")
            menu()
        if newGrade <= 8 or newGrade >= 13:
            print("\nInvalid\n")
            menu()
        firstName.append(newFirstName)
        lastName.append(newLastName) 
        studentGrade.append(newGrade)
        studentNumber.append(studentNumber[-1]+1)
        print("\n"+ str(newFirstName), newLastName, "has been added\n\n")
        menu()
        
def modifyAStudent():
    while True:
        print("\n\n")
        ModTitle = "MODIFY A STUDENT" 
        print(ModTitle.rjust(31))
        print(("=" * len(ModTitle) + "\n").rjust(32))
        modifyNumber = input("Enter the student number of the student to modify: ")
        try:
            int(modifyNumber)
            modifyNumber= int(modifyNumber)
            
        except:
            print("\nInvalid\n")
            menu()
            
        if modifyNumber > len(firstName):
            print("\nInvalid\n")
            menu()
        modifyNumber = modifyNumber-1
        print("Modify", firstName[modifyNumber], str(lastName[modifyNumber]) + "?")
        YesOrNo = input("(Y)es or (N)o: ").upper()
        
        if YesOrNo == "N":
            menu()
        
        if YesOrNo != "N" and YesOrNo != "Y":
            print("\nInvalid\n")
            menu()
        
        if modifyNumber < 0 or modifyNumber >= len(firstName):
            print("\nInvalid\n")
            menu()
        
        modFirstName = input("\nEnter the first name: ").title()
        
        if modFirstName.isalpha() == False:
            print("\nInvalid\n")
            menu()
            
        modLastName = input("Enter the last name: ").title()
        
        if modLastName .isalpha() == False:
            print("\nInvalid\n")
            menu()
            
        oldFirst = firstName[modifyNumber]
        oldLast = lastName[modifyNumber]
        firstName[modifyNumber] = modFirstName
        lastName[modifyNumber] = modLastName
        print()
        print(oldFirst, oldLast,"has been renamed to", firstName[modifyNumber], lastName[modifyNumber], "\n\n")
        menu()

def findNumber():
    while True:
        print("\n")
        FindTitle = "FIND A STUDENT TITLE" 
        print(FindTitle.rjust(31))
        print(("=" * len(FindTitle) + "\n").rjust(32))
        findFirstName = input("Enter the first name: ").title()
        
        if findFirstName.isalpha() == False:
            print("\nInvalid\n")
            menu()
            
        findLastName = input("Enter the last name: ").title()
        
        if findLastName.isalpha() == False:
            print("\nInvalid\n")
            menu()
            
        for i in range(len(firstName)):
            if firstName[i] == findFirstName and lastName[i] == findLastName:
                print()
                print(firstName[i], lastName[i], "in grade", studentGrade[i], "has student number:", studentNumber[i], "\n\n")
                menu()
        print("\nNo student by that name\n\n")
        menu()

#Start of code with number of students
while True:
    Students = input("Enter the number of students in the school: ")
    print("\n")
    try:
        int(Students)
        Students = int(Students)
        if Students <= 0:
            print("Invalid\n")
            continue
        break
    except:
        print("Invalid\n")
        

randomStudents(Students)       
menu()

