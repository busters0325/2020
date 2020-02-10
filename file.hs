import System.IO  
import Control.Monad
import Data.List.Split
import Data.Vector as V
import Data.Typeable

main = do  
        let list = []
        handle <- openFile "test.txt" ReadMode
        contents <- hGetContents handle
        let singlewords = words contents
            list = f singlewords
        let a = Data.List.Split.chunksOf 10 list
        print a
        let b = V.toList $ V.fromList [ V.fromList [1|x<-[1..10]]|x<-[1..10] ]
        let c = [ V.fromList [1|x<-[1..10]]|x<-[1..10] ]
        print a
        print b
        print c
	print $ typeOf a
        --print $ typeOf b
        --print $ typeOf c
        hClose handle   

f :: [String] -> [Int]
f = Prelude.map read

