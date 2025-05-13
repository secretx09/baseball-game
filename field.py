
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
        if base_num == 2:
            self.second_base = "@"
        if base_num == 3:
            self.third_base = "@"

    def empty_base(self, base):
        if base == 0:
            self.first_base = " "
            self.second_base = " "
            self.third_base = " "
        if base == 1:
            self.first_base = " "
        if base == 2:
            self.second_base = " "
        if base == 3:
            self.third_base = " "