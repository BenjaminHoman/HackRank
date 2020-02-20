import Control.Applicative
import Control.Monad
import System.IO
import Data.List(group)

remainderDrop stride xs = let l=length xs; r=l `mod` stride 
                            in drop (l-r) xs
remainderDrop2 = remainderDrop 2

reduceStr [] = "Empty String"
reduceStr str 
    | isReduced = str
    | otherwise = reduceStr . concat $ map remainderDrop2 groups
    where
        groups = group str
        isReduced = length groups == (sum $ map length groups)

main :: IO ()
main = do
    s <- getLine
    putStrLn $ reduceStr s

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret          

