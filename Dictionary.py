string='''The Taj Mahal was commissioned by Shah Jahan in 1631, to be built in the memory of his wife Mumtaz Mahal, who died on 17 June that year while giving birth to their 14th child, Gauhara Begum.[10][11] Construction started in 1632, and the mausoleum was completed in 1648, while the surrounding buildings and garden were finished five years later.[12][13]

The imperial court documenting Shah Jahan's grief after the death of Mumtaz Mahal illustrates the love story held as the inspiration for the Taj Mahal.[14] According to contemporary historians Muhammad Amin Qazvini, Abdul Hamid Lahori and Muhammad Saleh Kamboh, Shah Jahan did not show the same level of affection for others as he had shown Mumtaz while she was alive. After her death, he avoided royal affairs for a week due to his grief and gave up listening to music and lavish dressing for two years. Shah Jahan was enamored by the beauty of the land at the south side of Agra on which a mansion belonging to Raja Jai Singh I stood. He chose the place for the construction of Mumtaz's tomb after which Jai Singh agreed to donate it to the emperor.[15]'''

list = string.split()
s= set(list)
dict={}
for x in s:
    dict[x]=0

for x in list:
    dict[x]+=1

print(dict)
