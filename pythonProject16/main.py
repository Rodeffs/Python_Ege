# def sum_range(start, end):
#     if start > end:
#         """
#         tmp = start  ------- Для замены значений для всех языков
#         start = end
#         end = tmp
#         """
#         end, start = start, end
#     return sum(range(start, end + 1))
#
#
# print(sum_range(1, 3))
#

def three_args(var1, var2=None, var3=None):
    if var2 is not None and var3 is not None:
        print(f"Переданы аргументы: var1 = {var1}, var2 = {var2}, var3 = {var3}")
    elif var2 is None and var3 is not None:
        print(f"Переданы аргументы: var1 = {var1}, var3 = {var3}")
    elif var2 is not None and var3 is None:
        print(f"Переданы аргументы: var1 = {var1}, var2 = {var2}")
    elif var2 is None and var3 is None:
        print(f"Переданы аргументы: var1 = {var1}")


three_args(var1=553, var3=3)
