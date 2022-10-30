import React from "react";
import { motion } from "framer-motion";

function Header() {
  return (
    <div className="bg-white">
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
                className="h-8 w-auto sm:h-10"
                src="/palm-tree_1f334.png"
                alt=""
              />
            </a>
          </div>
          <div>
            <a
            href="https://xenseee.tech" className="italic text-xs lg:text-2xl ">
            Created by <span className="text-blue-500 font-semibold">Jabed</span>
            </a>
          </div>
        </motion.div>
      </div>
    </div>
  );
}

export default Header;
