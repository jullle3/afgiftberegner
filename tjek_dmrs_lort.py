import csv
import re


def print_stats(reader):
    counter = 0
    total_price = 0
    total_model_year = 0
    min = [10000000000] # noget skal det jo være mindre end:)
    max = [0]

    for row in reader:
        total_model_year += int(re.findall('[0-9]+', row[7])[0]) # finder modelår
        price = int(row[11].replace(".", ""))  # finder pris
        total_price += price

        # TODO: Ikke pythonic, benyt max og og sort med iterators
        # find min, og gem reference til det givne row
        if price > max[0]:
            max = [price, row]

        # find max
        if min[0] > price:
            min = [price, row]

        counter += 1
    # calculate results
    print(f'Avg price: {total_price//counter} dkk')
    print(f'Avg model year: {total_model_year/counter:.6}')
    print(f'Most expensive car: {max[1][11]} dkk, originally bought for {max[1][10]} in {max[1][7]} ')
    print(f'Cheapest car: {min[1][11]} dkk, originally bought for {min[1][10]} in {min[1][7]} ')


def print_by_cheapest(reader):
    a = sorted(reader, key=lambda x: int(x[11].replace(".", "")))
    print(f'Imported as {1:>15} Handelspris {1:<15} Originally bought for (dkk) {1:<10} Year {1:<10} Afgift udgør')
    for car_data in a:
        tax = int(car_data[13].replace(".", ""))
        car_value = int(car_data[12].replace(".", ""))
        print(f'{car_data[11]:<20} {car_data[12].replace(".", ""):<34} {car_data[10]:<40} {car_data[7]:<15} {tax/car_value*100:.4}% ')


def main():
    with open("C:\\Users\\julle\\Desktop\\afgiftberegner\\DMR-vurderinger\\rs6.csv", encoding="utf-8") as f_in:
        reader = csv.reader(f_in, delimiter=";")
        next(reader)  # skip header
        print_by_cheapest(reader)


main()
