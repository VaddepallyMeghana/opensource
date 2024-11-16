vignesh, charan = input().split()
if vignesh == charan:
    print("NULL")
elif (vignesh == 'R' and charan == 'S') or (vignesh == 'P' and charan == 'R') or (vignesh == 'S' and charan == 'P'):
    print("Vignesh")
else:
    print("Charan")
