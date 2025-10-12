letter = ''' Dear <|Name|>,
            You are selected !
            <|Date|> '''

print(letter.replace("<|Name|>", "Faisal").replace("<|Date|>", "20-10-26"))
