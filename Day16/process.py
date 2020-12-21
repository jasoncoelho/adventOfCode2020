
import os
import sys
import re

rules = []
optimizedRules  = list()

def mergeIntervals(rules):

    sortedRules = sorted(rules,key=lambda x: x[0])

    print(sortedRules)
    
    for cur_start,cur_end,_ in sortedRules:
        if len(optimizedRules) == 0:
            optimizedRules.append((cur_start,cur_end))
        else:
            start,end = optimizedRules.pop()
            if end >= cur_start: # check for overlap
                # and also if the overlap extends over the next interval
                optimizedRules.append((start,cur_end if cur_end > end else end))
            else:
                optimizedRules.append((start,end)) # since there is no peek
                optimizedRules.append((cur_start,cur_end))

    print(f"interval stack = {optimizedRules}")


with open(os.path.join(sys.path[0],"rules.txt")) as rules_file:

    # arrival location: 28-928 or 943-952
    rule_pattern = "(.*)\:\s(\d+)-(\d+)\sor\s(\d+)-(\d+)"

    for rule_line in [ line.rstrip() for line in rules_file.readlines() ]:
        
        match = re.match(rule_pattern,rule_line)

        field_name = match.group(1)
        r1_start,r1_end = int(match.group(2)), int(match.group(3))
        r2_start,r2_end = int(match.group(4)), int(match.group(5))

        print(f"{field_name} {r1_start}-{r1_end} or {r2_start}-{r2_end}")

        rules += [ ( r1_start,r1_end,field_name), (r2_start,r2_end,field_name) ]
    
    print(rules)
    
    mergeIntervals(rules)


def isValid(value):

    for (start,end) in optimizedRules:
        if start <= int(value) <= end:
            return True
    return False

with open(os.path.join(sys.path[0],"nearby_tickets.txt")) as rules_file:

    scanning_error_rate = 0

    valid_tickets = []

    for values_ticket in [ line.rstrip().split(',') for line in rules_file.readlines() ]:
        
        invalid_values = [ int(value) for value in values_ticket if not isValid(value)]

        # print(invalid_values)

        if not len(invalid_values):
            valid_tickets += [ values_ticket ]

        scanning_error_rate += sum(invalid_values)

    print(f"scanning error rate: {scanning_error_rate}") # 21081


    # first determine possible description within each field type by intersecting
    # against previously guessed descriptions for that field
    
    ticket_field_guesses = dict()

    for index,valid_ticket in enumerate(valid_tickets):

        for field_index,field_value in enumerate(valid_ticket):
            
            guesses = { desc for (start,end,desc) in rules if start <= int(field_value) <= end }
            
            current_guesses = ticket_field_guesses.get(field_index)

            if  current_guesses == None:    
                ticket_field_guesses[field_index] = guesses # initialize
            elif len(current_guesses) > 1:
                # intersect and eliminate guesses that are no longer valid
                ticket_field_guesses[field_index] = current_guesses.intersection(guesses)

    
    # keys sorted by number of guesses 
    keys = [item[0] for item in sorted(ticket_field_guesses.items(), key=lambda item: len(item[1]))]
      
    # start with the smallest guess (1 if the data set is correct), and eliminate 
    # that guess from the remainder of the other field's guesses, and repeat for the remaining
    seen = set()

    for index,key in enumerate(keys):

        current_guesses = ticket_field_guesses[key] - seen

        for k in keys[index+1:]:
            ticket_field_guesses[k] -= current_guesses

        seen |= current_guesses

        print(ticket_field_guesses)
        print(seen)
        print()

    
    product = 1
    my_ticket = [73,101,67,97,149,53,89,113,79,131,71,127,137,61,139,103,83,107,109,59]
    for k,v in ticket_field_guesses.items():
        # if 'departure' in v:
        departures = [val for val in v if 'departure' in val]
        if len(departures) > 0:
            product *= my_ticket[k]

    print(product)


# thoughts
# - check for overlap and if that overlap encompasses the next interval
# - when eliminating guesses, need to check across fields in addition to within each field
           