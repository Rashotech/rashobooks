import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://ttdyeradcauljg:0c2870d53600062a44fce328cc5b837e60e86f5a1fc1e47a80b63fe1e6eaa505@ec2-3-211-48-92.compute-1.amazonaws.com:5432/d95ge10rl45mqt")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"Added {title} written by {author} with isbn {isbn} in the year {year}.")
    print("All books added")
    db.commit()

if __name__ == "__main__":
    main()