import os

#Define the class structure for CSV Validator

class CSVValidator:
  
  def __init__(self, input_file, output_file , expected_columns=3):
    self.input_file = input_file
    self.output_file = output_file
    self.expected_columns = expected_columns
    self.total_rows_processed = 0
    self.valid_rows_count = 0
    self.header = ""
    self.clean_data = []
    
  # New Method Placeholder: We will define this validation logic next.
  
  def _is_row_valid(self, row):
    """Checks if a row meets all validation criteria."""
    return True  # For now, we'll assume every row is valid
  
  def run(self):
    """
    The main method to execute the validation process (UPDATED).
    """
    print(f" Starting Validation For {self.input_file} ---")
    
     # 1. Read the input file line by line
    try:
      
      with open(self.input_file , "r") as infile :
        
        for line in infile:
          # Strip leading/trailing whitespace and remove the newline character
          raw_row = line.strip()
          
          if not raw_row :
            continue  #skips empty lines 
          
          #Seperate Header logic 
          
          if self.total_rows_processed == 0 :
            self.header = raw_row 
            self.clean_data.append(raw_row) #add the raw line if valid
          else:
            #split the line into  fields and check validity
            fields = raw_row.split(',')  
            
            if self._is_row_valid(fields):
              self.valid_rows_count += 1
              self.clean_data.append(raw_row) # adds the raw line if valid
              
            
          self.total_rows_processed += 1 
        
    except FileNotFoundError:
      print(f"ERROR: Input file '{self.input_file}' not found.")
      return
    
    
    #write the clean data  to the output file
    
    with open(self.output_file ,"w") as outfile :  
      for row in self.clean_data:
        outfile.write(row + '\n')
    
    
    
    print(f"Total rows processed : {self.total_rows_processed} ")    
    print(f"Valid rows : {self.valid_rows_count} ")     
    print(f"Validation Complete. Clean data saved to {self.output_file}")  
    
    
if __name__ == "__main__":
  validator = CSVValidator("sample_data.csv", "clean_data.csv") 
  validator.run()
     
  
    
  

