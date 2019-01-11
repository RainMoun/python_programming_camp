l=[1,2,10,30,33,99,101,200,301,402]

def search(num,l,start=0,stop=len(l)-1):
    if start <= stop:
        mid=start+(stop-start)//2
        print('start:[%s] stop:[%s] mid:[%s] mid_val:[%s]' %(start,stop,mid,l[mid]))
        if num > l[mid]:
            start=mid+1
        elif num < l[mid]:
            stop=mid-1
        else:
            print('find it',mid)
            return
        search(num,l,start,stop)
    else: #如果stop > start则意味着列表实际上已经全部切完，即切为空
        print('not exists')
        return

search(301,l)

# 对比下
index_301 = l.index(301)
print(index_301)
# 实现类似于l.index(301)的效果