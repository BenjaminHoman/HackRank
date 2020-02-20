import Control.Applicative
import Control.Monad
import System.IO
import Data.Set(fromList, size)

findScores fn xs = size $ fromList $ scanl1 fn xs
getHighest xs = findScores max xs - 1
getLowest xs = findScores min xs - 1

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    score_temp <- getLine
    let score = map read $ words score_temp :: [Int]
    -- your code goes here
    putStrLn $ (show $ getHighest score) ++ " " ++ (show $ getLowest score)

getMultipleLines :: Int -> IO [String]
getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret      