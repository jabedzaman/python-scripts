import React from "react";
import { motion } from "framer-motion";

const scripts = [
  {
    name: "ATM clone",
    description:
      "A replica of ATM for a single user, let's say, Mr. John, who has already successfully logged into his account on the ATM Machine, now, we will program the next steps he may want to perform.  Like display his name and cash available in his savings account Withdraw cash and display the status of the cash balance. Deposit cash and display the status of the cash balance.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/ATM%20Clone/atmclone.py",
  },
  {
    name: "Acronymn Generator",
    description:
      "a python script that generates an acronym word from a given sentence.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Acronym%20Generator/acronymngenerator.py",
  },
  {
    name: "Cake cutter",
    description:
      "find if it is possible to cut the cake in the below mentioned ways for a given value of N. Given an integer N and a cake which can be cut into pieces, each cut should be a straight line going from the center of the cake to its border.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Cake%20Cutter/cakecutter.py",
  },
  {
    name: "Clock Angle",
    description:
      "Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Clock%20Angle/clockangle.py",
  },
  {
    name: "Contact Book",
    description:
      "a repository of your classmates name and mobile numbers. And whenever you want to search the mobile/contact number of some of your classmate, you can easily search it out from the repository you maintained",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Contact%20List/contactlist.py",
  },
  {
    name: "Currency Convertor",
    description:
      "a python script that converts the currency of one country to another country.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Currency%20Convertor/currencyconvertor.py",
  },
  {
    name: "Egg Arranger",
    description:
      "Given a number N, find the number of ways to arrange N eggs in a matrix",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Egg%20Arranger/eggarranger.py",
  },
  {
    name: "Email Slicer",
    description:"Email Slicer is just a simple tool that will take multiple email address as an input and slice it to produce the username and the domain associated with it. The email must be divided into two strings by using @ as the separator",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Email%20Slicer/emailslicer.py"
  },
  {
    name: "Fibonacci Series",
    description:"In this project user will enter single or multiple numbers and your system will predict that the entered number or number’s is/are valid number(s) in a Fibonacci series or not.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Fibonacci%20Series/fibonacciseries.py"
  },
  {
    name: 'Leap year calclator',
    description: 'a functionality in which when user will input a range of two dates. Then your module will find and print all years in the range of given dates those are leap years separately and rest of the years those are non-leap separately.',
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Leap%20Year%20Range/leapyearrange.py"
  },
  {
    name: 'Life Duration Calculator',
    description: 'a python script that calculates the life duration of a person.',
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Life%20Duration%20Calculator/lifedurationcalculator.py"
  },
  {
    name: 'Multiplication Table',
    description: 'a multiplication table application where user will enter a sentinel value n and the application will display the mathematical multiplication tables till given sentinel value n',
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Multiplication%20Table/multiplicationtable.py"
  },
  {
    name: "Number Checker",
    description: "enter a range [A, B] and system will randomly pick any number from your given range and check the status of that given number",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Number%20Checker/numberchecker.py"
  },
  {
    name: 'Number Guess Game',
    description: 'a script that generates a random number between a fixed range, and  if the user guesses the number right in three chances, then user wins otherwise user lose',
    url: 'https://github.com/jabedzaman/python-scripts/blob/master/Number%20Guess/numberguess.py'
  },
  {
    name: 'Palindrome Number',
    description: 'a program to find the nth prime palindrome number, n is the input user will give.',
    url: 'https://github.com/jabedzaman/python-scripts/blob/master/Palindrom%20Number/palindrome.py'
  },
  {
    name: 'Password Generator',
    description: 'a python script that generates a random password for the user.',
    url: 'https://github.com/jabedzaman/python-scripts/blob/master/Password%20Generator/passwordgenrator.py'
  },
  {
    name: 'Prime Number Checker',
    description: 'enter a positive integer range [A, B] and system will find out the status (Prime or composite) of each number available in the given range. At the end print the count also.',
    url: 'https://github.com/jabedzaman/python-scripts/blob/master/Prime%20Composite/primecomposite.py'
  },
  {
    name: 'Random Story generator',
    description: 'a python script that generates a random story for the user.',
    url: 'https://github.com/jabedzaman/python-scripts/blob/master/Random%20Story/randomstory.py'
  },
  {
    name: 'Rank & Mark',
    description: 'a python script that calculates the rank and mark of a student.',
    url: 'https://github.com/jabedzaman/python-scripts/blob/master/Rank%20and%20Mark%20calculator/rankmarkcalculator.py'
  },
  {
    name: 'Rock Paper Scisoors',
    description: 'a python script that plays rock paper scissors with the user.',
    url: 'https://github.com/jabedzaman/python-scripts/blob/master/Rock%20Paper%20Scissors/rockpaperscissors.py',
  },
  {
    name: 'Rolling Dice',
    description: 'input user will give a static number (between 1 to 6) and then roll the dice which randomly generate some value between 1 to 6. The winning situation arrives when the given static/fixed number exactly same to the number came after rolling the dice',
    url: 'https://github.com/jabedzaman/python-scripts/blob/master/Rolling%20Dice/rollingdice.py'
  },
  {
    name: 'Scientific Calculator',
    description: 'a python script that performs scientific calculations.',
    url: 'https://github.com/jabedzaman/python-scripts/blob/master/Scientific%20Calculator/scientificcalculator.py'
  }
];

function Item() {
  return (
    <section className="text-gray-600 body-font overflow-hidden">
      <div className="container px-5 py-24 mx-auto">
        <div className="-my-8 divide-y-2 divide-gray-100">
          {scripts.map((item) => (
            // eslint-disable-next-line react/jsx-key
            <motion.div 
            initial={{
                opacity: 0,
                y: 100
            }}
            whileInView={{
                opacity: 1,
                y: 0
            }}
            exit={{
                opacity: 0,
                y: 100
            }}
            transition={{
                duration: 0.5
            }}
            className="py-8 flex flex-wrap md:flex-nowrap">
              <div className="md:flex-grow">
                <h2 className="text-2xl font-medium text-gray-900 title-font mb-2">
                  {item.name}
                </h2>
                <p className="leading-relaxed">{item.description}</p>
                <a
                  href={item.url}
                  className="text-indigo-500 inline-flex items-center mt-4"
                >
                  Source Code
                  <svg
                    className="w-4 h-4 ml-2"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="2"
                    fill="none"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path d="M5 12h14"></path>
                    <path d="M12 5l7 7-7 7"></path>
                  </svg>
                </a>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Item;
