import Control.Applicative
import Control.Monad
import System.IO
import Data.List(group, sort)

tally xs = map (\x -> (head x, length x)) $ (group . sort) xs

pairs xs = sum $ map (\(i, count) -> if mod count 2 == 0 then (count `div` 2) else (count-1) `div` 2) $ tally xs

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    ar_temp <- getLine
    let ar = map read $ words ar_temp :: [Int]
    
    putStrLn $ show $ pairs ar

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret   