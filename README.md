## **分析目標**

找出商品被購買的關聯性

## **資料集**

![image](https://github.com/Jiahsiu/transaction_association/blob/main/截圖%202024-01-30%20上午1.57.11.png)
> 紀錄每筆交易的商品項目及購買時間

## **前處理**

![image](https://github.com/Jiahsiu/transaction_association/blob/main/imag/截圖%202024-01-30%20上午1.10.49.png)
>1、 處理Item左右空格  
>2、 將Transaction有空值的行刪去  
>3、 將Transaction那列的整數值轉為字串

![image](https://github.com/Jiahsiu/transaction_association/blob/main/imag/截圖%202024-01-30%20上午1.10.59.png)

![image](https://github.com/Jiahsiu/transaction_association/blob/main/imag/截圖%202024-01-30%20上午1.11.05.png)

![image](https://github.com/Jiahsiu/transaction_association/blob/main/imag/截圖%202024-01-30%20上午1.11.12.png)
> 定義hot_encode function

## **實作結果**
![image](https://github.com/Jiahsiu/transaction_association/blob/main/imag/截圖%202024-01-30%20上午1.11.34.png)
>1、 從confidence可以看出，在所有交易中， 有大約70.3%的機率顧客在購買Spanish Brunch的同時也會購買Coffee  
>2、 從lift可以看出，在所有交易中，這種組合比隨機機率高出51.16%  
>-> 由此即可知曉兩項商品被購買的關聯性
