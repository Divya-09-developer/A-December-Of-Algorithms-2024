def find_missing_bib_no(bib_no,n):
    expect_sum=n*(n+1)//2
    act_sum=sum(bib_no)
    miss_bib_no=expect_sum-act_sum
    return miss_bib_no
N=5
bib_no=[1,2,4,5]
print("The missing bib number is",find_missing_bib_no(bib_no,N))