first_base = " "
second_base = " "
third_base = " "
home_plate = " "

class Field():
  baseball_field = f"""                                    
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
            .%%.                                  -{second_base}{second_base}-                                  .%%.          
              :@#                               :{second_base}{second_base}{second_base}{second_base}{second_base}{second_base}:                               #@:            
                -@*                              *{second_base}{second_base}{second_base}{second_base}*                              *@-              
                  +@=                          -@* -- *@-                          =@+                
                    *@:                      .@%        %@.                      :@*                  
                    .#@:                  .%%.          .%%.                  .@#.                   
                      :%#.               *@-              -@*               .#%:                     
                        -@*            =@=                  =@=            *@-                       
                          =@=        -@*                      *@-        =@=                         
                            *@- . :@#          .*%%*.          #@: .  -@*                           
                              .{third_base}{third_base}{third_base}{third_base}.           +@@@@@@+          {first_base}{first_base}{first_base}{first_base}                           
                            :{third_base}{third_base}{third_base}{third_base}{third_base}{third_base}-          @@@@@@@@          -{first_base}{first_base}{first_base}{first_base}{first_base}{first_base}:                            
                                {third_base}{third_base}{third_base}            *@@@@@@*            {first_base}{first_base}{first_base}                              
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

  print(baseball_field)