import Control.Applicative
import Control.Monad
import System.IO

combinations xs ys = [(x,y) | x <- xs, y <- ys]

maxSpent keyboards drives s = maximum $ map fn $ combinations keyboards drives
    where fn (k, d) = if k+d <= s then k+d else -1


main :: IO ()
main = do
    s_temp <- getLine
    let s_t = words s_temp
    let s = read $ s_t!!0 :: Int
    let n = read $ s_t!!1 :: Int
    let m = read $ s_t!!2 :: Int
    keyboards_temp <- getLine
    let keyboards = map read $ words keyboards_temp :: [Int]
    drives_temp <- getLine
    let drives = map read $ words drives_temp :: [Int]
    --  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    putStrLn $ show $ maxSpent keyboards drives s

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret          

