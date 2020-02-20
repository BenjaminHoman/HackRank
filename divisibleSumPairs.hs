import Control.Applicative
import Control.Monad
import System.IO
import Data.List(tails)

combinations 0 _  = [[]]
combinations n xs = [y:ys | y:xs' <- tails xs, ys <- combinations (n-1) xs']

enCombinations n = combinations n . zip [0..]
        
filtered k = length . filter fn . enCombinations 2
    where fn ((i,a):(j,b):[]) = i < j && mod (a + b) k == 0

main :: IO ()
main = do
    n_temp <- getLine
    let n_t = words n_temp
    let n = read $ n_t!!0 :: Int
    let k = read $ n_t!!1 :: Int
    ar_temp <- getLine
    let ar = map read $ words ar_temp :: [Int]
    putStrLn $ show $ filtered k ar

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret     