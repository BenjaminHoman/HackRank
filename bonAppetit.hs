import Control.Applicative
import Control.Monad
import System.IO

realCost items k = fst . foldl1 aggr $ zip items [0..]
    where aggr (total,_) (cost, i) = if i/=k then (total+cost,i) else (total,i)

diff items k total = if total == real then "Bon Appetit" else show . abs $ total - real
    where real = (realCost items k) `div` 2

main :: IO ()
main = do
    n_temp <- getLine
    let n_t = words n_temp
    let n = read $ n_t!!0 :: Int
    let k = read $ n_t!!1 :: Int
    ar_temp <- getLine
    let ar = map read $ words ar_temp :: [Int]
    b_temp <- getLine
    let b = read b_temp :: Int
    
    putStrLn $ diff ar k b

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret          

