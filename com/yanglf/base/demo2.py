# 定义 list
entity = ['zs']
# 添加一组数据到数组
entity.extend(['1', 890, ['joke', 250], 23.09])
print(entity)
# 添加一个元素到数组
entity.append('李四')
# 将数据添加到数据第一个元素位置
entity.insert(0, '张三')
print(entity)
# 删除元素
entity.remove('zs')
print(entity)
# 删除元素
del entity[0]
print(entity)
item = entity.pop(1)
print('删除元素:{},下标:1'.format(item))
# 列表切片
lst = entity[1:3]
print(lst)
