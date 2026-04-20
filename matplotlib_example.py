import matplotlib.pyplot as plt

categories = ['SQL', 'Python', 'Power BI', 'Ai']
values = [31, 14, 15, 26]

plt.bar(categories, values, color='#04A5F8')
plt.title('Tools used in job postings')
plt.ylabel('Percentage %')
plt.show()