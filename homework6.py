blog_views=[150,800,2500,600,1200,450,3000]
total_view=0
count_trending=0
for i in blog_views:
    if i>1000:
        print("Trending")
        count_trending=count_trending+1
    elif i>=500 and i<=1000:
        print("Average")
    else:
        print("Low Traffic")
    total_view=total_view+i
print("Total number of views:",total_view)
print("Posts that were Trending:",count_trending)