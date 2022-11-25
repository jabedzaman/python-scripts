import React from "react";
import GitHubButton from "react-github-btn";
import { motion } from "framer-motion";
import { useTheme } from "next-themes";

function Hero() {
  const { theme } = useTheme();
  return (
    <div className="mt-10 px-6">
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <center>
        <a href="https://github.com/jabedzaman/python-scripts">
          <motion.img
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
            src="https://raw.githubusercontent.com/jabedzaman/readme-logos/main/assets/language/python.svg"
            className="w-48 h-48 lg:w-80 lg:h-80"
            alt="Python-Scripts"
          />
        </a>
        <motion.h1
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
        className="lg:text-4xl text-2xl font-semibold lg:font-bold mt-10 mb-10">
          Python Scripts
        </motion.h1>
        <motion.p
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
        className="lg:text-lg text-sm mt-10 mb-20">
          A collection of Python scripts created for fun and learning purposes.
        </motion.p>
        <hr className="text-gray-200 dark:text-gray-900 mb-20" />
      </center>
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
        className="flex mt-4 flex-col max-w-2xl justify-center items-center space-y-2 mx-auto"
      >
        <div className="flex flex-row  space-x-2">
          {/* <!-- Place this tag where you want the button to render. --> */}
          <GitHubButton
            href="https://github.com/jabedzaman"
            data-color-scheme="no-preference: light; light: light; dark: light;"
            data-size="large"
            aria-label="Follow @jabedzaman on GitHub"
          >
            Follow @jabedzaman
          </GitHubButton>
          <GitHubButton
            href="https://github.com/HOSENUR"
            data-color-scheme="no-preference: light; light: light; dark: light;"
            data-size="large"
            aria-label="Follow @HOSENUR on GitHub"
          >
            Follow @HOSENUR
          </GitHubButton>
        </div>
        <div className="flex flex-row  space-x-2">
          {/* <!-- Place this tag where you want the button to render. --> */}
          <GitHubButton
            href="https://github.com/jabedzaman/python-scripts"
            data-color-scheme="no-preference: light; light: light; dark: light;"
            data-icon="octicon-star"
            data-size="large"
            aria-label="Star jabedzaman/python-scripts on GitHub"
          >
            Star
          </GitHubButton>
          {/* <!-- Place this tag where you want the button to render. --> */}
          <section className="">
            <GitHubButton
              href="https://github.com/jabedzaman/python-scripts/fork"
              data-color-scheme="no-preference: light; light: light; dark: light;"
              data-icon="octicon-repo-forked"
              data-size="large"
              aria-label="Fork jabedzaman/python-scripts on GitHub"
            >
              Fork
            </GitHubButton>
          </section>
          <div className="hidden lg:inline">
            {/* <!-- Place this tag where you want the button to render. --> */}
            <GitHubButton
              href="https://github.com/jabedzaman/python-scripts/subscription"
              data-color-scheme="no-preference: light; light: light; dark: light;"
              data-icon="octicon-eye"
              data-size="large"
              aria-label="Watch jabedzaman/python-scripts on GitHub"
            >
              Watch
            </GitHubButton>
          </div>
          {/* <!-- Place this tag where you want the button to render. --> */}
          <div className=" ">
            <GitHubButton
              href="https://github.com/jabedzaman/python-scripts/discussions"
              data-color-scheme="no-preference: light; light: light; dark: light;"
              data-icon="octicon-comment-discussion"
              data-size="large"
              aria-label="Discuss jabedzaman/python-scripts on GitHub"
            >
              Discuss
            </GitHubButton>
          </div>
        </div>
      </motion.div>
    </div>
  );
}

export default Hero;
