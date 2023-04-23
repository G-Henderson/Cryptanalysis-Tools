def get_permutations(characters, permutation_length: int=None) -> list:
        """
        Gets the permutations 
        """

        # Create list to store permutations in
        my_permutations = []
        
        # Check the permutation length
        num_chars = len(characters)
        if (permutation_length == None):
            permutation_length = num_chars

        
        indices = [i for i in range(num_chars)]
        cycles = [i for i in range(num_chars, num_chars-permutation_length, -1)]
        
        # Add first permutation
        my_permutations.append([characters[i] for i in indices[:permutation_length]])
        
        while True:
            for i in range(permutation_length-1, -1, -1):
                cycles[i] -= 1
                
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = num_chars - i
                    
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    
                    my_permutations.append([characters[i] for i in indices[:permutation_length]])
                    
                    break
            
            else:
                return my_permutations
            
print(get_permutations(list("ABCD"), 2))