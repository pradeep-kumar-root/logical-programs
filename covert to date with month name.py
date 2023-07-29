import calendar
date_ip = input("Enter date in dd/mm/yy format: ")
lt = date_ip.split("/")
print(lt)

print("{} {} {}".format(str(lt[0]),str(calendar.month_name[int(lt[1])]),str(lt[2]))) #calendar.month_name[month_number]
                                                                                     
