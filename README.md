# Commission Bot for GTA RP Discord

This Discord bot is being used in a GTA RP discord server for a jewelry store. It's only purpose is to calculate commission for each individual employee for the week.

## How it works
This bot takes in the message history from a individual employee's sales channel within the server. It then takes the role from the command and calculates the commission based off of the percentage of each gem or chain sale.

## Command
The only command for this bot is 'commission'. This command is followed by a specific role for the employee. The only roles are:
+ jewel - Jewel Inspector
+ shift - Shift Lead
+ manager - Manager
Each role gets a different percentage of commission. 

## Example message history
> gem 14500<br/>
> gem 29500<br/>
> chain 300000<br/>
> chain 150000

## Example command use
> commission jewel

## Example return message
> 139400.0
