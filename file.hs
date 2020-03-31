import System.IO  
import Control.Monad
import Data.List.Split
import Data.Vector as V
import Data.Typeable

main = do  
        let list = []
        handle <- openFile "read.txt" ReadMode
        contents <- hGetContents handle
        let singlewords = words contents
            list = f singlewords




	--problem
        let a = Data.List.Split.chunksOf 10 list
        let b = V.toList $ V.fromList [ V.fromList [1|x<-[1..10]]|x<-[1..10] ]
        let c = [ V.fromList [1|x<-[1..10]]|x<-[1..10] ]
        print list
	print $ typeOf list
        print a
        print $ typeOf a
        print b
        --print $ typeOf b
        print c
        --print $ typeOf c
        hClose handle   


f :: [String] -> [Int]
f = Prelude.map read

