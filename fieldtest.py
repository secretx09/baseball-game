# field.py

home_plate = " "

class Field():
    def __init__(self):
        self.first_base = " "
        self.second_base = " "
        self.third_base = " "
        self.display()

    def display(self):
        self.baseball_field = f"""                                    
                                                      ..                                                 
                                          :+#@@@@@%**++===+**%@@@@@%+:                                    
                                    -*%@#+-.                        .-+#@%*-                              
                              .=@@#-                                      -#@@=.                         
                            :@@#.                                              .#@@:                      
                        =@@-                                                      -@@=                   
                      :%@=                                                            =@%:                
                    =@#                                                                  #@=              
                  *@=                                                                      =@#            
                *@-                                                                          -@*          
              #@:                                      .                                     :@#         
                .%%.                                  -{self.second_base}{self.second_base}-                                  .%%.          
                  :@#                               :{self.second_base}{self.second_base}{self.second_base}{self.second_base}{self.second_base}{self.second_base}:                               #@:            
                    -@*                              *{self.second_base}{self.second_base}{self.second_base}{self.second_base}*                              *@-              
                      +@=                          -@* -- *@-                          =@+                
                        *@:                      .@%        %@.                      :@*                  
                        .#@:                  .%%.          .%%.                  .@#.                   
                          :%#.               *@-              -@*               .#%:                     
                            -@*            =@=                  =@=            *@-                       
                              =@=        -@*                      *@-        =@=                         
                                *@- . :@#          .*%%*.          #@: .  -@*                           
                                  .{self.third_base}{self.third_base}{self.third_base}{self.third_base}.           +@@@@@@+          {self.first_base}{self.first_base}{self.first_base}{self.first_base}                           
                                :{self.third_base}{self.third_base}{self.third_base}{self.third_base}{self.third_base}{self.third_base}-          @@@@@@@@          -{self.first_base}{self.first_base}{self.first_base}{self.first_base}{self.first_base}{self.first_base}:                            
                                    {self.third_base}{self.third_base}{self.third_base}            *@@@@@@*            {self.first_base}{self.first_base}{self.first_base}                              
                                    :. -@*          :*@@*:          *@- :.                               
                                          +@=                      =@+                                    
                                            *@:                  :@*                                      
                                            .#@.              :@#.                                       
                                              :%#.          .#%:                                         
                                                -@*        *@-                                           
                                                  =@= :: =@=
                                                    *{home_plate}{home_plate}{home_plate}{home_plate}*                                               
                                                  :{home_plate}{home_plate}{home_plate}{home_plate}{home_plate}{home_plate}:                                              
                                                    -{home_plate}{home_plate} =                                                 
                                                      .
                                                                                                                                                                          
        """
        print(self.baseball_field)

    def fill_base(self, base_num):
        if base_num == 1:
            self.first_base = "@"
        elif base_num == 2:
            self.second_base = "@"
        elif base_num == 3:
            self.third_base = "@"
        self.print_players_on_base()  # Call the new method to print players on base

    def empty_base(self, base):
        if base == 0:
            self.first_base = " "
            self.second_base = " "
            self.third_base = " "
        elif base == 1:
            self.first_base = " "
        elif base == 2:
            self.second_base = " "
        elif base == 3:
            self.third_base = " "

    def print_players_on_base(self):
        players_on_base = 0
        if self.first_base == "@":
            players_on_base += 1
        if self.second_base == "@":
            players_on_base += 1
        if self.third_base == "@":
            players_on_base += 1
        
        print(f"Players on base: {players_on_base}")
