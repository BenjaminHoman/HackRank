import Control.Applicative
import Control.Monad
import System.IO
import Data.List(sortBy)
import Data.Ord(compare)
import Data.Map (Map)
import qualified Data.Map as Map

insertBird bird tally = Map.insert bird occurance tally
    where occurance = case Map.lookup bird tally of 
                        Just a -> a+1 
                        Nothing -> 1

countTypes [] tally = tally
countTypes (x:birds) tally = countTypes birds (insertBird x tally)

getCommonBird birds = fst $ head $ sortBy orderFn $ Map.toList tally
    where 
        tally = countTypes birds Map.empty
        orderFn (k1,v1) (k2,v2) = let keyComp=compare k1 k2; valComp=compare v2 v1 in
                                    if valComp == EQ then keyComp else valComp

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    ar_temp <- getLine
    let ar = map read $ words ar_temp :: [Int]
    putStrLn $ show $ getCommonBird ar

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret       