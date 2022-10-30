import React from "react";
import GitHubButton from "react-github-btn";
import { motion } from "framer-motion";

function Hero() {
  return (
    <div>
      {/* eslint-disable-next-line @next/next/no-img-element */}
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
          src="https://ik.imagekit.io/jabedzaman/Python_Scripts/Python_Scripts_Wez3Xcy23.png?ik-sdk-version=javascript-1.4.3&updatedAt=1667035157365"
          alt="Python-Scripts"
        />
      </a>
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
      className="flex flex-row max-w-2xl justify-evenly mx-auto">
      {/* <!-- Place this tag where you want the button to render. --> */}
      <GitHubButton
        href="https://github.com/jabedzaman"
        data-color-scheme="no-preference: light; light: light; dark: light;"
        data-size="large"
        aria-label="Follow @jabedzaman on GitHub"
      >
        Follow @jabedzaman
      </GitHubButton>
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
      <GitHubButton
        href="https://github.com/jabedzaman/python-scripts/fork"
        data-color-scheme="no-preference: light; light: light; dark: light;"
        data-icon="octicon-repo-forked"
        data-size="large"
        aria-label="Fork jabedzaman/python-scripts on GitHub"
      >
        Fork
      </GitHubButton>
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
      {/* <!-- Place this tag where you want the button to render. --> */}
      <GitHubButton
        href="https://github.com/jabedzaman/python-scripts/discussions"
        data-color-scheme="no-preference: light; light: light; dark: light;"
        data-icon="octicon-comment-discussion"
        data-size="large"
        aria-label="Discuss jabedzaman/python-scripts on GitHub"
      >
        Discuss
      </GitHubButton>
      </motion.div>
    </div>
  );
}

export default Hero;
