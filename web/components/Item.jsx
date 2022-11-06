import React from "react";
import { motion } from "framer-motion";

const scripts = [
  {
    name: "ATM clone",
    description:
      "A clone of simple ATM. Performs basic action.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/ATM%20Clone/atmclone.py",
  },
  {
    name: "Acronymn Generator",
    description:
      "A python script that generates an acronym word from a given sentence.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Acronym%20Generator/acronymngenerator.py",
  },
  {
    name: "BMI Calculator",
    description: "A python script to calculate the bmi",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/BMI%20Calculator/bmicalculator.py",
  },
  {
    name: "Cake cutter",
    description:
      "A python script to divde cake in equal no of pieces",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Cake%20Cutter/cakecutter.py",
  },
  {
    name: "Clock Angle",
    description:
      "A python script to find the angle between the hands of the clock",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Clock%20Angle/clockangle.py",
  },
  {
    name: "Contact Book",
    description:
      "It stores the name of the contact with number and then later can be used to filter and search",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Contact%20List/contactlist.py",
  },
  {
    name: "Currency Convertor",
    description:
      "A python script that converts the currency of one country to another country.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Currency%20Convertor/currencyconvertor.py",
  },
  {
    name: "Current Weather",
    description: "Uses openweather API to find the weather of the current location",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Weather/weather.py",
  },
  {
    name: "Egg Arranger",
    description:
      "Arranges the input number of eggs in a matrix form",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Egg%20Arranger/eggarranger.py",
  },
  {
    name: "Email Slicer",
    description:
      "Email Slicer is just a simple tool that will take multiple email address as an input and slice it to produce the username and the domain associated with it.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Email%20Slicer/emailslicer.py",
  },
  {
    name: "Fibonacci Series",
    description:
      "Check numbers whether is in  fibonacci series",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Fibonacci%20Series/fibonacciseries.py",
  },
  {
    name: "Income Tax Calculator",
    description: "Calculates the tax one has to pay",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Income%20Calculator/incometaxcalculator.py",
  },
  {
    name: "Insta DP Viewer",
    description: "Script to view the instagram dp of someone",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Insta%20DP/instadp.py",
  },
  {
    name: "JPG convertor",
    description: "A python Script to  convert an image to jpg format",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/JPG%20convertor/jpgconvertor.py",
  },
  {
    name: "Leap year calclator",
    description:
      "Find the leap years between two input dates.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Leap%20Year%20Range/leapyearrange.py",
  },
  {
    name: "Life Duration Calculator",
    description:
      "A python script that calculates the life duration of a person.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Life%20Duration%20Calculator/lifedurationcalculator.py",
  },
  {
    name: "Multiplication Table",
    description:
      "Builds multiplication table of input number",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Multiplication%20Table/multiplicationtable.py",
  },
  {
    name: "Number Checker",
    description:
      "Provides you with the data of a random number",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Number%20Checker/numberchecker.py",
  },
  {
    name: "Number Guess Game",
    description:
      "Number guessing game in python",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Number%20Guess/numberguess.py",
  },
  {
    name: "Palindrome Number",
    description:
      "A program to find the nth prime palindrome number, n is the input user will give.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Palindrom%20Number/palindrome.py",
  },
  {
    name: "Password Generator",
    description:
      "A python script that generates a random password for the user.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Password%20Generator/passwordgenrator.py",
  },
  {
    name: "Prime Number Checker",
    description:
      "Checks wether number is prime or not.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Prime%20Composite/primecomposite.py",
  },
  {
    name: "Random Story generator",
    description: "A python script that generates a random story for the user.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Random%20Story/randomstory.py",
  },
  {
    name: "Rank & Mark",
    description:
      "A python script that calculates the rank and mark of a student.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Rank%20and%20Mark%20calculator/rankmarkcalculator.py",
  },
  {
    name: "Rock Paper Scisoors",
    description:
      "A python script that plays rock paper scissors with the user.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Rock%20Paper%20Scissors/rockpaperscissors.py",
  },
  {
    name: "Rolling Dice",
    description:
      "Rolling dice game in python",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Rolling%20Dice/rollingdice.py",
  },
  {
    name: "Scientific Calculator",
    description: "A python script that performs scientific calculations.",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Scientific%20Calculator/scientificcalculator.py",
  },
  {
    name: "Wifi Password",
    description:
      "Used to extract the pssword of the networks you were connected till the past",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/WiFi%20Password/wifipassword.py",
  },
  {
    name: "Word Counter",
    description: "Used to count the words of a txt file",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Word%20Counter/wordcounter.py",
  },
  {
    name: "Youtube Video Downloader",
    description: "Used to download youtube vidoes",
    url: "https://github.com/jabedzaman/python-scripts/blob/master/Youtube%20Video%20Downloader/youtubevideodownloader.py",
  },
];

function Item() {
  return (
    <section className="text-gray-600 dark:text-neutral-300 body-font overflow-hidden">
      <div className="container px-5 py-24 mx-auto">
        <div className="-my-8 divide-y-2 divide-gray-100">
          {scripts.map((item) => (
            // eslint-disable-next-line react/jsx-key
            <motion.div
              initial={{
                opacity: 0,
                y: 100,
              }}
              whileInView={{
                opacity: 1,
                y: 0,
              }}
              exit={{
                opacity: 0,
                y: 100,
              }}
              transition={{
                duration: 0.5,
              }}
              className="py-8 flex flex-wrap md:flex-nowrap"
            >
              <div className="md:flex-grow">
                <h2 className="text-2xl font-medium text-gray-900 dark:text-white title-font mb-2">
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
