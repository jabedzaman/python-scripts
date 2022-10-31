import React from "react";
import { motion } from "framer-motion";
import { useTheme } from 'next-themes'


function Header() {
  const { theme, setTheme } = useTheme()
  return (
    <div className="bg-white dark:bg-black">
      <div className="max-w-7xl mt-0 mx-auto px-4 sm:px-6">
        <motion.div
          initial={{
            opacity: 0,
            y: -100,
          }}
          animate={{
            opacity: 1,
            y: 0,
          }}
          transition={{
            duration: 1,
            delay: 0.2,
          }}
          className="flex justify-between items-center border-b-2 border-gray-100 py-6 md:justify-start md:space-x-10">
          <div className="flex justify-start lg:w-0 lg:flex-1">
            <a
              href="#">
              <span className="sr-only">Jabed Zaman</span>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                className="h-8 w-auto sm:h-10 dark:rounded-lg"
                src="/palm-tree_1f334.png"
                alt=""
              />
            </a>
          </div>
          <div onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')} className="cursor-pointer border rounded-full bg-neutral-200 dark:bg-neutral-800 w-10 h-10 flex items-center justify-center text-2xl">

            {theme === 'light' ? <i className="bi bi-brightness-high-fill"></i> : <i className="bi bi-moon-stars-fill"></i>}
          </div>
          <div>
            <section
               className="italic text-xs lg:text-2xl ">
              Created by <a href="https://xenseee.tech" className="text-blue-500 font-semibold">Jabed</a> and <a href="https://hosenur.dev" className="text-blue-500 font-semibold">Hosenur</a>
            </section>
          </div>
        </motion.div>
      </div>
    </div>
  );
}

export default Header;
