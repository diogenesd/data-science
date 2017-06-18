

# Access direct
def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # todo: return the correct value
    return days_in_month[month_number - 1]

# This test case should print 31, the number of days in the eighth month,
# August


print(how_many_days(8))

# Slice
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

# Mutabilite
dish = [
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "baked beans",
    "Spam",
    "Spam",
    "Spam",
    "Spam"]
mr_buns_order = dish
print(dish)
print(mr_buns_order)
dish[6] = "Spam"  # baked beans are off
print(mr_buns_order)
print(dish)


# Function MAx_VALUE numbers
batch_sizes = [15, 6, 89, 34, 65, 35]
max(batch_sizes)

# Funciton MAX_VALUE strings: return max by ord (ASCII)
python_varieties = [
    'Burmese Python',
    'African Rock Python',
    'Ball Python',
    'Reticulated Python',
    'Angolan Python']
max(python_varieties)

# Function MIN_VALUE numbers
min(batch_sizes)

# Funciton MIN_VALUE strings: return max by ord (ASCII)
min(python_varieties)

# Function Join in lists
nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)


# Top three
def top_three(input_list):
    """Returns a list of the three largest elements
        input_list in order from largest to smallest.

        If input_list has fewer than three elements,
        return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    return sorted(input_list, reverse=True)[:3]


print(top_three([2, 3, 5, 6, 8, 4, 2, 1]))


# Median
def median(numbers):
    numbers.sort()  # The sort method sorts a list directly,
    # rather than returning a new sorted list
    if(len(numbers) % 2 == 0):
        middle_index = int(len(numbers) / 2)
        return (numbers[middle_index] + numbers[middle_index - 1]) / 2
    middle_index = int(len(numbers) / 2)
    return numbers[middle_index]


test1 = median([1, 2, 3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1, 2, 3, 4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))


# Titles
names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']

for name in names:
    print(name.title())


"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and end with a right angle bracket ">".
"""
# TODO: Define the tag_count function


def tag_count(tags):
    sum = 0
    for tag in tags:
        if(tag[0] == "<" and tag[-1] == ">"):
            sum += 1
    return sum

# Test for the tag_count function:


list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))


# define the  html_list function
def html_list(words):
    string = ""
    string += "<ul>\n"
    for word in words:
        string += "<li>{}</li>\n".format(word)
    string += "</ul>"
    return string


print(html_list(['first string', 'second string']))

# Starbox


def starbox(width, height):
    """imprime uma caixa feita e asteriscos.

    width: comprimento da caixa em caracteres, deve ser ao menos 2
    height: altura da caixa em linhas, deve ser ao menos 2
    """
    print("*" * width)  # imprime a ponta superior da caixa

    # imprime os lados da caixa
    for _ in range(height - 2):
        print("*" + " " * (width - 2) + "*")

    print("*" * width)  # imprime a ponta inferior da caixa


starbox(6, 6)


def box(width, height, symbol="*"):
    """Imprimir uma caixa composta de asteriscos, ou algum outro caractere.

    width: Largura da caixa em caracteres, deve ser pelo menos 2
    height: Altura da caixa em linhas, deve ser pelo menos 2
    symbol: Uma única sequência de caracteres usada para
    desenhar as bordas da caixa
    """
    print(symbol * width)  # imprimir borda superior da caixa

    # print sides of box
    for _ in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)

    print(symbol * width)  # imprimir borda inferior da caixa


box(5, 5)
box(5, 5, "$")

# BlackJack
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) <= 21:
    hand.append(card_deck.pop())

print(hand)


# TODO: Implement the nearest_square function
def nearest_square(limit):
    nearest = 0
    while(nearest**2 < limit):
        nearest += 1
    return (nearest - 1)**2


test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))


# ship's weigth
# cada item do manifest é um item e seu peso
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels", 42], [
    "machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

cargo_weight = 0
cargo_hold = []

for cargo in manifest:
    if cargo_weight >= 100:
        break
    else:
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]
