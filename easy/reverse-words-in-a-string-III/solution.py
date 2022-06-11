 def reverseWords(self, s):
        def reverseHelper(s):
            s_reversed = ""    
            for i in range(len(s)-1, -1, -1):
              s_reversed += s[i]
            return s_reversed

        combined_string  = ""

        i = 0
        j = 0
        n = len(s)-1

        while (i <= n):
          if (j != n):
            if (s[j] == " "):
              combined_string += reverseHelper(s[i:j]) + " "
              j = j + 1
              i = j
            else:
              j += 1

          else:
            combined_string += reverseHelper(s[i:j+1])
            break


        return combined_string
