# Assign the sentence to a variable
fox_statement="The!quick!brown!fox!jumps!over!the!lazy!dog."
# Remove all "!" and replace these with a space
fox_statement_update=fox_statement.replace("!"," ")
# Convert the sentence to uppercase
fox_statement_upper=fox_statement_update.upper()
print(f"{fox_statement_update}"
      f"\n{fox_statement_upper}"
      # Print the sentence in reverse order
      f"\n{fox_statement_update[::-1]}"
      )
