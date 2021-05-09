from random import shuffle
import argparse
import logging

logging.basicConfig(filename="clean_emails.log", level=logging.INFO, format="%(asctime)s %(message)s")

logging.debug("Debug")
logging.info("Info message")
logging.warning("Warning")
logging.error("Błąd")
logging.critical("Critical message")

parser = argparse.ArgumentParser()
parser.add_argument("-g", action="store_true")
parser.add_argument("-o", "--outfile")
parser.add_argument("-f", "--infile")

args = parser.parse_args()

def generate_data(n):
    logging.info(f"Generuję {n} zestawów emaili ")
    emails = []
    for i in range(n):
        email = f"user-{i+1}@email.com"
        emails.append(email)
        emails.append(email)
        emails.append(" " + email)
        emails.append(email.upper())
        emails.append(f"user-{i+1}email.com")
        emails.append(f"user-{i+1}@@email.com")

    shuffle(emails)

    try:
        1/0
    except:
        logging.error("Wystąpił błąd", exc_info=True)
    return emails

def save_data(data, f_name):
    with open(f_name, "w") as f:
        for d in data:
            f.write(d+"\n")

def clean(data):
    output = set()
    for el in data:
        if el.count("@") == 1:
            output.add(el.lower().strip())

    return sorted(output, key=lambda x: int(x.split("-")[1].replace("@email.com", "")))

def main():
    if args.g:
        data = generate_data(10)
        save_data(data, args.outfile)
    else:
        with open(args.infile) as f:
            data = f.read().splitlines()
            cleaned = clean(data)

        save_data(cleaned, args.outfile)


if __name__ == "__main__":
    main()