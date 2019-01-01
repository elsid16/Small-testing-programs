import itertools

#INPUTS{
Number_of_items=int(input("Number of items: "))
Number_of_min_items_to_get_free=int(input("Buy these many clothes: "))
Number_of_free_items=int(input("To get free these many clothes: "))
discount_rate=float(input("Discount rate: "))
price=[]
for j in range(Number_of_items):
    price.append(float(input("Cost of cloth", j, ": ")))
#}
'''
#tries{
Number_of_items=2
Number_of_min_items_to_get_free=3
Number_of_free_items=2
discount_rate=20
price=[200,100]
#}
'''
if Number_of_items<Number_of_min_items_to_get_free+Number_of_free_items:
    print(sum(price)-sum(price)*discount_rate/100)
    quit()
all_possible_permutations_price=list(itertools.permutations(price))
#print(list(all_possible_permutations_price))
detail_of_iteration=[]
'''
for j in range(len(all_possible_permutations_price)):
    detail_of_iteration.append([all_possible_permutations_price[j][0]+all_possible_permutations_price[j][1]+all_possible_permutations_price[j][2]-min(all_possible_permutations_price[j][:3])-all_possible_permutations_price[j][3]*discount_rate/100+all_possible_permutations_price[j][3],all_possible_permutations_price[j][0],all_possible_permutations_price[j][1],all_possible_permutations_price[j][2],all_possible_permutations_price[j][3]])
print(sorted(detail_of_iteration))
'''

final_cost_and_details_all_iterations=[]
r=Number_of_items%(Number_of_min_items_to_get_free + Number_of_free_items)
for i in range(0,Number_of_items//Number_of_min_items_to_get_free+Number_of_free_items,Number_of_min_items_to_get_free+Number_of_free_items):
    for j in range(len(all_possible_permutations_price)):
        start_of_offer_lot=0
        end_of_offer_lot=Number_of_min_items_to_get_free+Number_of_free_items
        cost_of_iteration=sum(all_possible_permutations_price[j])
        cost=list(all_possible_permutations_price[j])
        for k in range(Number_of_items//(Number_of_min_items_to_get_free+Number_of_free_items)-i):
            least=sorted(all_possible_permutations_price[j][start_of_offer_lot:end_of_offer_lot])
            #print(all_possible_permutations_price[j][start_of_offer_lot:end_of_offer_lot])
            #cost_of_iteration-=least
            free_items=least[:Number_of_free_items]
            cost_of_iteration-=sum(free_items)
            start_of_offer_lot+=Number_of_min_items_to_get_free+Number_of_free_items
            end_of_offer_lot+=Number_of_min_items_to_get_free+Number_of_free_items
            detail_of_iteration.append("Neglected: ")
            detail_of_iteration.append(free_items)
        for k in range(Number_of_items-(Number_of_items%(Number_of_min_items_to_get_free+Number_of_free_items)),Number_of_items):
            cost_of_iteration-=all_possible_permutations_price[j][k]*discount_rate/100
            #print(all_possible_permutations_price[j][k])
            detail_of_iteration.append("On discount: ")
            detail_of_iteration.append(all_possible_permutations_price[j][k])
        #print(cost_of_iteration)
        #print()
        g=[cost_of_iteration]   #change float variable to list for appending details
        g.extend(detail_of_iteration)
        final_cost_and_details_all_iterations.append(g)
final_cost_and_details_all_iterations=sorted(final_cost_and_details_all_iterations)
for i in range(len(final_cost_and_details_all_iterations)):
    print(final_cost_and_details_all_iterations[i])
